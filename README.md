# Cardekho Dataset - Car Price Prediction

## Overview

This project revolves around predicting car prices using the Cardekho dataset. The primary objective is to leverage machine learning techniques to determine optimal prices for cars based on various features.

## Getting Started

### Prerequisites

Ensure you have the following prerequisites installed on your system:

- Python 3.x
- Jupyter Notebook
- Required libraries: pandas, numpy, scikit-learn, seaborn, matplotlib

### Installation

1. Clone the repository:

    ```bash
    git clone [https://github.com/your-username/cardekho-car-price-prediction.git](https://github.com/avinashnethaa/Attempt1.git)
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Project Workflow

### 1. Data Exploration

- Import necessary libraries to facilitate data analysis.
- Check the shape of the dataset to understand its dimensions (`df.shape`).
- Examine unique values in categorical columns (`df['column'].unique()`).
- Identify and analyze null values within the dataset (`df.isnull().sum()`).

### 2. Exploratory Data Analysis (EDA)

- Explore dataset statistics to gain insights into central tendencies and variability (`df.describe()`).
- Visualize feature correlations using seaborn heatmap (`sns.heatmap()`).
- Handle null values, making data suitable for further analysis, and save in `Final_dataset`.

### 3. Feature Engineering

- Find the current year as a reference for car age calculation.
- Calculate the age of each car based on the manufacturing year.
- Drop irrelevant columns that do not contribute significantly to the analysis (`df.drop(['column1', 'column2'], axis=1, inplace=True)`).
- Apply one-hot encoding to categorical features for machine learning compatibility (`pd.get_dummies()`).

### 4. Data Preparation

- Separate independent variables (features) and the target variable (car prices).

### 5. Feature Importance

- Utilize RandomForestRegressor to determine the importance of each feature (`ExtraTreesRegressor()`).
- Visualize feature importance using a bar chart for a clearer understanding of influential factors.

### 6. Model Training

- Train a Random Forest Regressor using the preprocessed dataset to predict car prices.

### 7. Model Persistence

- Save the trained model using Pickle, allowing for easy retrieval and future use (`with open('random_forest_regression_model.pkl', 'wb')`).

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The Cardekho dataset for providing valuable data for analysis.
- The developers and contributors of the libraries and tools used in this project.
