# Kaggle GoDaddy - Microbusiness Density Forecasting

---

### Resources

Competition link: [Here](https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting)

Hottest EDA (as of 01/20/2023): [Here](https://www.kaggle.com/code/imnaho/eda-predict)

Modeling Comparison (Most informative one in my opinion): [Here](https://www.kaggle.com/code/kimtaehun/complete-baseline-code-with-various-ml-model#notebook-container)

### External Data Sources: 

1. [Summary post](https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/discussion/372604)
2. [County Transportation Profiles](https://data.bts.gov/Research-and-Statistics/County-Transportation-Profiles/qdmf-cxm3)
3. [@KAGGLEQRDL posted](https://www.kaggle.com/datasets/kaggleqrdl/gd2022datasets/code)
4. [Federal Reserve Economic Data](https://fred.stlouisfed.org/)

data/external:
- [population_data.csv](https://www.kaggle.com/datasets/ruslansadykov/population-data-for-godaddy)
- [county-neighbours.csv](https://www.kaggle.com/datasets/ruslansadykov/population-data-for-godaddy)

### Tools

1. [Pandas-profiling](https://github.com/ydataai/pandas-profiling)
2. [Dataprep](https://github.com/sfu-db/dataprep)
3. [Sweetviz](https://github.com/fbdesignpro/sweetviz)
4. [Pycaret](https://github.com/pycaret/pycaret)
5. [Hyperopt AutoML](https://github.com/hyperopt/hyperopt)

---

### Kick-off
1. Create virtual environment ```python<version> -m venv <venv name>```
2. Upgrade pip and install requirement packages ```pip install --upgrade -r requirements.txt```
3. Create a new branch and start to work on it ```git checkout -b <branch name>```

### Development
1. EDA
2. Feature Engineering (WIP)
3. Model Development (Pending)
4. Model tuning (Pending)

### Wrap-up
1. Create submission (Pending)
2. Generate requirements with [pipreqsnb](https://pypi.org/project/pipreqsnb/): ``` pipreqsnb <project_path>```