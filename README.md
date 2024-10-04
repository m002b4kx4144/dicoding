# Dicoding Collection Dashboard ✨

Welcome to the Dicoding Collection Dashboard! This project helps to analyze and visualize data using an interactive Streamlit dashboard.

## Setup Environment - Anaconda

To set up your environment using Anaconda, follow these steps:

```sh
conda create --name main-ds python=3.12
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

If you're using a standard shell/terminal setup, here’s how to prepare the environment:

```sh
mkdir dicoding
cd dicoding
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Streamlit App

To run the Streamlit app for the dashboard:

```sh
streamlit run dashboard/dashboard.py
```

## Folder Structure

This project has the following folder structure:

```
submission
├───dashboard
|     ├───day.csv
|     ├───hour_clean.csv
|     └───dashboard.py
├───data
|     ├───day.csv
|     └───hour.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
```

- **dashboard/**: Contains the main data (`day.csv` and `hour_clean.csv`) used for visualizations and the Streamlit app script (`dashboard.py`).
- **data/**: This folder includes additional data files (`day.csv` and `hour.csv`) that are used in the analysis.
- **notebook.ipynb**: Jupyter Notebook used for exploratory data analysis (EDA).
- **README.md**: The file you are currently reading, providing project setup and usage instructions.
- **requirements.txt**: Lists all dependencies required for the project.
- **url.txt**: Contains any reference URLs or sources used in the project.

## Dependencies

Make sure you have all the dependencies installed by using the commands above to set up your environment. The dependencies are listed in `requirements.txt`.