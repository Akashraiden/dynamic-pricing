# End-to-End-ML-Driven Dynamic Pricing for Sustainable Product Markets

## Overview

This project focuses on developing a dynamic pricing strategy for sustainable products in the market. The goal is to predict optimal prices using machine learning models, considering factors like demand elasticity, competitor prices, inventory levels, and eco-friendly certifications.

## Data Description

The dataset contains information about various products and includes the following columns:
- **Product_ID**: A unique identifier for each product.
- **Product_Name**: The name or description of the product.
- **Category**: The product category (e.g., Personal Care, Stationery, Household).
- **Base_Price**: The original price of the product before adjustments.
- **Demand_Elasticity**: A measure of how sensitive the product's demand is to price changes.
- **Seasonal_Factor**: A factor indicating the effect of seasonal trends on demand.
- **Competitor_Price**: The price of similar products from competitors.
- **Inventory_Level**: The available stock of the product.
- **Customer_Rating**: The average rating given by customers.
- **Green_Certification**: A binary indicator showing if the product is eco-friendly (1 = Certified, 0 = Non-Certified).
- **Profit_Margin**: The percentage of profit earned on the product.
- **Inventory_Risk**: The calculated risk associated with the product’s inventory levels.
- **Adjusted_Elasticity**: A refined version of demand elasticity considering market factors.
- **Competitor_Price_Difference**: The difference between the product price and competitor prices.
- **Green_Certification_Label**: A label indicating the type of certification (Certified or Non-Certified).

## Exploratory Data Analysis (EDA)

The first phase of the project involved **Exploratory Data Analysis (EDA)** to understand the dataset, identify patterns, and check for any inconsistencies or anomalies. Key steps included:
- **Analyzing the distribution** of key variables such as `Base_Price`, `Demand_Elasticity`, and `Inventory_Level`.
- **Performing correlation analysis** to explore relationships between variables like `Competitor_Price` and `Profit_Margin`.
- **Handling missing values** and outliers.
- **Visualizing data** using **matplotlib** and **seaborn** for better insights.

For a detailed breakdown of the **EDA** process, including the code, visualizations, and specific steps taken, please refer to the `eda.ipynb` file located in the project directory.

## Feature Engineering

During the feature engineering phase, several transformations were applied to improve the model's performance:
- **Creating new features** such as `Adjusted_Elasticity` and `Competitor_Price_Difference` to better capture market dynamics.
- **Encoding categorical variables** like `Category` and `Green_Certification` using **one-hot encoding**, **label encoding**, and leveraging **CatBoost** for native handling.
**Standard Scaling** was applied to continuous variables: `Competitor_Price`, `Profit_Margin`, `Inventory_Level`, `Inventory_Risk`, and `Adjusted_Elasticity` to standardize them. This transformation removes the mean and scales the data to unit variance.
.

The detailed feature engineering steps and code for these transformations are available in the `eda.ipynb` file. Please refer to it for a comprehensive view of the process.

## Machine Learning Models

This project utilizes several machine learning models for demand prediction and price optimization:
- **CatBoostRegressor**: A gradient boosting algorithm designed for categorical features.
- **AdaBoostRegressor**: A boosting algorithm that combines weak models to create a strong model.
- **GradientBoostingRegressor**: A machine learning technique for regression tasks using an ensemble of decision trees.
- **RandomForestRegressor**: An ensemble method that builds multiple decision trees and averages their predictions.
- **LinearRegression**: A linear approach to modeling the relationship between the target variable and one or more features.
- **DecisionTreeRegressor**: A decision tree algorithm for regression tasks.
- **XGBRegressor**: A gradient boosting method, optimized for speed and performance in regression tasks.

## Variables

In this project, the **dependent variable** (target) and **independent variables** (features) have been defined as follows:

#### Dependent Variable
- **Base_Price**: The target variable that we are trying to predict. It represents the original price of the product before any dynamic pricing adjustments.

#### Independent Variables
The following features are used as independent variables to predict the **Base_Price**:
- **Competitor_Price**: The price of a similar or equivalent product offered by competitors in the market.
- **Profit_Margin**: The profit percentage earned on the product relative to its cost.
- **Inventory_Level**: The current stock available for the product, measured in quantity.
- **Inventory_Risk**: A calculated measure of the risk associated with holding inventory for the product, influenced by stock levels and demand trends.
- **Adjusted_Elasticity**: A refined version of demand elasticity, adjusted for additional market or behavioral factors.
- **Category**: The product category to which the product belongs (e.g., Personal Care, Stationery, Household).
- **Green_Certification_Label**: The eco-friendly certification label for the product (e.g., "Certified", "Non-Certified").
- **Product_Name**: The name or title of the product.

These independent variables are used in conjunction to build and train the machine learning models for predicting the **Base_Price**.

## Technologies Used

This project utilizes the following libraries and tools:

### Programming and Data Analysis
- **pandas**: Data manipulation and analysis.
- **numpy**: Numerical computations.

### Visualization
- **seaborn**: Statistical data visualization.
- **matplotlib**: Plotting and chart creation.

### Machine Learning
- **scikit-learn**: Model building and evaluation.
- **xgboost**: Gradient boosting for demand prediction.
- **catboost**: Handling categorical features in machine learning.

### Serialization
- **dill**: Enhanced serialization of Python objects.

### Development Tools
- **VS Code**: Code editing and debugging.

## File Organization

This project follows an **end-to-end** approach, including data ingestion, data transformation, model training, logging, and exception handling. Below is a description of the key files and their functions:

- **`data_ingestion.py`**: Handles the process of loading and ingesting raw data into the system, preparing it for further analysis.
- **`data_transformation.py`**: Contains functions for cleaning and transforming the data, such as handling missing values, feature encoding, and scaling.
- **`model_trainer.py`**: Defines and trains machine learning models, evaluates their performance, and saves the trained models for future use.
- **`exception.py`**: Custom exception handling file that ensures errors during the process are caught and logged effectively.
- **`logger.py`**: Manages logging to track the flow of the application, making it easier to debug and monitor.
- **`utils.py`**: Includes helper functions used throughout the project, such as loading configuration settings, saving models, and making predictions.
- **`app.py`**: The main script that ties all the components together, running the data ingestion, transformation, model training, and predictions in a sequential manner.


## Results



## Model Performance

The models were evaluated using key performance metrics, including **R² Score**, **Mean Absolute Error (MAE)**, and **Root Mean Squared Error (RMSE)**. Below is a summary of their performance:

| **Model**                | **R² Score** | **MAE**       | **RMSE**      |
|--------------------------|--------------|---------------|---------------|
| **Linear Regression**     | 0.7855       | 9.0011        | 11.5675       |
| **Decision Tree**         | 0.9882       | 1.8701        | 2.7130        |
| **Random Forest**         | 0.9950       | 1.0652        | 1.7672        |
| **Gradient Boosting**     | 0.9869       | 2.2622        | 2.8559        |
| **Support Vector Regressor** | 0.9393     | 4.3349        | 6.1537        |
| **XGBoost**               | 0.9963       | 1.1372        | 1.5143        |
| **CatBoost**              | 0.9988       | 0.6492        | 0.8603        |
| **AdaBoost**              | 0.8717       | 7.1752        | 8.9442        |

### Key Observations:
- **CatBoost** achieved the best overall performance, with the highest **R² score (0.9988)** and the lowest errors (**MAE: 0.6492**, **RMSE: 0.8603**), making it the most effective model for predicting **Base_Price**.
- **XGBoost** also performed exceptionally well, with an **R² score of 0.9963**, **MAE: 1.1372**, and **RMSE: 1.5143**, making it a strong competitor to CatBoost.
- **Random Forest** and **Gradient Boosting** also delivered high performance, demonstrating good predictive power with **R² scores** of **0.9950** and **0.9869**, respectively.
- **AdaBoost** and **Support Vector Regressor** showed relatively weaker performance with **R² scores** of **0.8717** and **0.9393**, and high error metrics (**MAE** and **RMSE**), suggesting they are not as suitable for this task.


### Conclusion:

Best Model found **CatBoost_Regressor** 

Accurarcy **98.05**

| **Actual Value** | **Predicted Value** | **Difference** |
|-------------------|---------------------|----------------|
| **1714**          | 38.98               | 38.5119        | 0.4681         |
| **1673**          | 12.74               | 12.5438        | 0.1962         |
| **4029**          | 88.62               | 88.5068        | 0.1132         |
| **511**           | 36.92               | 37.2829        | -0.3629        |
| **843**           | 21.72               | 21.5549        | 0.1651         |

#### Utilized Streamlit for designing an interactive and user-friendly web interface.


<img src="images\Screenshot 2025-01-01 233912.png" alt="Image Description" width="500" height="500">

<img src="images\Screenshot 2025-01-01 233942.png" alt="Image Description" width="500" height="500">
