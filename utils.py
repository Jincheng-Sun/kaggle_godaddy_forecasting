import numpy as np
import pandas as pd


def random_masking(df, columns: list, random_seed: int = 42, n_rep: int = 1, threshold: float = 0.5,
                   include_origin: bool = True) -> pd.DataFrame:
    replicas = []
    np.random.seed(random_seed)
    mask_idx = np.random.random([n_rep, len(df), len(columns)]) > threshold
    for n in np.arange(n_rep):
        df_copy = df.copy()
        df_copy[columns] = df_copy[columns].mask(mask_idx[0])
        replicas.append(df_copy)
    if include_origin:
        replicas.append(df)
    return pd.concat(replicas)


def transpose_columns(df, idx: str = None, columns: list = None, col_f: callable = None) -> pd.Series:
    df_copy = df.copy()
    if idx is not None:
        df_copy = df_copy.set_index()
    if columns is not None:
        df_copy = df_copy[columns]
    if col_f is not None:
        df_copy.columns = df_copy.columns.map(col_f)
    return df_copy.stack()
