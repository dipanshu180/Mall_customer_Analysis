# Mall Customer Segmentation

## Overview
This project performs customer segmentation using **K-Means Clustering** based on **Age, Annual Income, and Spending Score**. The dataset used is `Mall_Customers.csv`.

## Features Used
- **Age**: Age of the customer.
- **Annual Income**: Customer's annual income.
- **Spending Score**: Score assigned based on customer behavior and spending patterns.

## Libraries Used
- **pandas**: Data manipulation
- **matplotlib**: Data visualization
- **seaborn**: Advanced data visualization
- **sklearn (scikit-learn)**: Machine learning algorithms

## Steps in Analysis
1. **Data Preprocessing**
   - Read the dataset
   - Handle missing values (if any)
   - Convert categorical data (Gender) into numerical format
   
2. **Data Visualization**
   - Distribution plots for Age, Annual Income, and Spending Score
   - Scatter plot of Annual Income vs Spending Score
   
3. **Feature Scaling**
   - Standardize the features using `StandardScaler`
   
4. **K-Means Clustering**
   - Apply K-Means with **5 clusters**
   - Visualize the clusters using a scatter plot

## How to Run the Project
1. Install the required dependencies:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
   ```
2. Run the Python script:
   ```bash
   python mall_customer_segmentation.py
   ```

## Visualization Outputs
- Histograms for **Age, Annual Income, and Spending Score**.
- Scatter plot showing **customer segmentation** based on **Annual Income vs Spending Score**.

## Results
Customers are segmented into **5 clusters**, which can help businesses understand different spending behaviors and target marketing strategies accordingly.

## Future Improvements
- Use **Elbow Method** or **Silhouette Score** to determine the optimal number of clusters.
- Apply **Hierarchical Clustering** for comparison.
- Perform **Dimensionality Reduction (PCA)** for better visualization.
