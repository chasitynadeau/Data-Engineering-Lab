import numpy as np
import pandas as pd
import argparse
from sklearn.preprocessing import StandardScaler

def main():
    parser = argparse.ArgumentParser(description = 'Data extract and transport app')
    parser.add_argument('command',
                       type = str,
                       help ='the command to run, either extract or transport')
    args = parser.parse_args()
    process(args.command)
    
def process(command):
    if command == "extract":
        file_path = (r"C:\Users\chasitynadeau\desktop\"Supermarket Sales.csv")
        df = pd.read_csv(file_path)
        df.columns(columns={'cogs': 'Cost of Goods Sold', 'gross margin percentage': 'Gross Margin Percentage', 'gross income': 'Gross Income'})
        clean_data_df = df.drop(columns=["Invoice ID","City","Product line", "Tax 5%", "Date", "Time", "Payment"])
        clean_data_df.to_csv("clean_data.csv", index = False, mode = 'w')
        
    elif command == "transform":
        clean_data_df = pd.read.csv("clean_data.csv")
        clean_data_df = pd.get_dummies(clean_data_df)
        
        scaler = StandardScaler()
        print(scaler.fit(clean_data_df))
        print(scaler.mean_)
        
        print(scaler.fit(clean_data_df))
        print(scaler.transform(clean_data_df))

        clean_data_df.to_csv("training_data.csv", index = False, mode = 'w')
        
main()
