"""
Sales Data Analysis
Author : Ansari Zaki
Date : 2/28/2026
Description : This script loads sales_data.csv, performs basic cleaning adn calculates key business metrics. 
"""

import pandas as pd

def load_data(filename):
    # Loads csv data into a pandas dataframe.
    try:
        dataFrame = pd.read_csv(filename)
        print(f"Data  loaded successfully from {filename}")
        return dataFrame
    except FileNotFoundError:
        print(f"File {filename} not found. Please check the path.")
        exit()

def clean_data(dataFrame):
    # Handles missing values and duplicates.
    print("\n-------------------- Data Cleaning --------------------")

    # Checks for missing values.
    missing = dataFrame.isnull().sum()
    if missing.sum() == 0:
        print("No missing values found.")
    else:
        print("Misssing values detected :")
        print(missing[missing > 0])
        dataFrame = dataFrame.dropna()
        print("Dropped rows with missing values.")

    # Checks for duplicates.
    duplicate = dataFrame.duplicated().sum()
    if duplicate == 0:
        print("No duplicate rows found.")
    else:
        print(f"Found {duplicate} duplicate rows.")
        dataFrame = dataFrame.drop_duplicates()

    return dataFrame

def analyze(dataFrame):
    # Calculate and return key metrics.

    # Basic statistics
    total_revenue = dataFrame["Total_Sales"].sum()
    total_quantity = dataFrame["Quantity"].sum()
    average_revenue = dataFrame["Total_Sales"].mean()

    # Best selling product by revenue.
    product_revenue = dataFrame.groupby("Product")["Total_Sales"].sum()
    best_revenue_product = product_revenue.idxmax()
    best_revenue_value = product_revenue.max()

    # Best selling product by quantity.
    product_quantity = dataFrame.groupby("Product")["Quantity"].sum()
    best_quantity_product = product_quantity.idxmax()
    best_quantity_value = product_quantity.max()

    # Packing matrics into a dictionary.
    metrics = {
        "Total Revenue (₹)" : f"{total_revenue:,.2f}" ,
        "Total Quantity Sold" : f"{total_quantity:,}" ,
        "Average Revenue per Sale (₹)" : f"{average_revenue:,.2f}" ,
        "Top Product by Revenue" : f"{best_revenue_product} (₹{best_revenue_value:,.2f})" ,
        "Top Product by Quantity" : f"{best_quantity_product} ({best_quantity_value} units.)"
    }

    return metrics

def print_report(metrics):
    # Displays the analysis results in a clean format.
    print("\n\n-------------------- SALES ANALYSIS REPORT --------------------\n")
    for key , value in metrics.items():
        print(f"{key:<30} {value:>30}")
    print("\n---------------------------------------------------------------\n")

def main():
    # Main program body.
    print("\n************************* SALES DATA ANALYSIS *************************\n")

    # Load.
    dataFrame = load_data("Internship\Week 3\sales_data.csv")

    # Explore.
    print("\n----- Data Overview -----")
    print(f"Shape : {dataFrame.shape}")
    print(f"Columns : {list(dataFrame.columns)}")

    # Clean.
    dataFrame = clean_data(dataFrame)

    # Analyze.
    metrics = analyze(dataFrame)

    # Report.
    print_report(metrics)

    print("\n***********************************************************************")

if __name__ == "__main__":
    main()