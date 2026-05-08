
import pandas as pd
from pathlib import Path

def load_data ():
    Base_DIR= Path.cwd()
    CSV1path= Base_DIR/"03_Library Systembook.csv"
    CSV2path= Base_DIR/"03_Library SystemCustomers.csv"
    "loading data"
    df1=pd.read_csv(CSV1path)
    df2=pd.read_csv(CSV2path)
    Summary = {
        "Dataset_1_total_rows":len(df1),
        "total_column_in_dataset1":len(df1.columns),
        "Missing_values_Datset1": df1.isna().sum().sum(),
        "Duplicate_values_Dataset1": df1.duplicated().sum(),
        "Dataset_2_total_rows":len(df2),
        "total_column_in_dataset2":len(df2.columns),
        "Missing_values_Datset2": df2.isna().sum().sum(),
        "Duplicate_values_Dataset2": df2.duplicated().sum()
    }
    summary_df=pd.DataFrame([Summary])
    summary_df.to_csv("Summary_report.csv")
    return df1, df2

df1,df2=load_data() 


def data_clean (df1,df2)->tuple:

    ##issues_in_df1=[df1[df1["Books"].isna() | df1["Customer ID"].isna()]].sum()

    ##print("Rows with missing values in Dataset 1")
    ##print(issues_in_df1)

    ##issues_in_df2=[df2[df2["Customer ID"].isna()]].sum()

    ##print("Rows with missing values in Dataset 2")
    ##print(issues_in_df2)

    df1["Book Returned"]=pd.to_datetime(df1["Book Returned"], format="%d/%m/%Y")
    df1["Book checkout"]=df1["Book checkout"].astype(str).str.replace("2063","2023")
    df1["Book checkout"]=pd.to_datetime(df1["Book checkout"].astype(str).str.replace('"','', regex=False), format="%d/%m/%Y", errors="coerce")

    
    df1.dropna(inplace=True)
    df1.reset_index(drop=True, inplace=True)

    df2.dropna(how="all", inplace=True)
    df2.reset_index(drop=True, inplace=True)
    Summary_1 = {
        "Dataset_1_total_rows":len(df1),
        "total_column_in_dataset1":len(df1.columns),
        "Missing_values_Datset1": df1.isna().sum().sum(),
        "Duplicate_values_Dataset1": df1.duplicated().sum(),
        "Dataset_2_total_rows":len(df2),
        "total_column_in_dataset2":len(df2.columns),
        "Missing_values_Datset2": df2.isna().sum().sum(),
        "Duplicate_values_Dataset2": df2.duplicated().sum()
    }
    summary_df1=pd.DataFrame([Summary_1])
    summary_df1.to_csv("Summary_report_after.csv")
    return df1,df2

df1,df2= data_clean(df1,df2)


df1.to_csv("clean_data.csv", index=False)
df2.to_csv("clean_data1.csv", index=False)
