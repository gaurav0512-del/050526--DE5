
import pandas as pd
from pathlib import Path



def load_data (file_path: str) -> pd.DataFrame

    "loading data"
    df1=pd.read_csv("03_Library Systembook.csv")
    df2=pd.read_csv("03_Library SystemCustomers.csv")
    return df1, df2
main()

def data_clean (df: )

issues_in_df1=[df1[df1["Books"].isna() | df1["Customer ID"].isna()]]

    print("Rows with missing values in Dataset 1")
    print(issues_in_df1)

        issues_in_df2=df2[df2["Customer ID"].isna()]

    print("Rows with missing values in Dataset 2")
    print(issues_in_df2)


    df1=df1.dropna(how="all")
    df1.reset_index(drop=True, inplace=True)

    df2=df2.dropna(how="all")
    df2.reset_index(drop=True, inplace=True)
     retrun df1, df2

def data_encrich (df1:pd.DataFrame):

    df1["Book Returned"]=pd.to_datetime(df1["Book Returned"], format="%d/%m/%Y")

    df1["Book checkout"]=pd.to_datetime(df1["Book checkout"].astype(str).str.replace('"','', regex=False), format="%d/%m/%Y", errors="coerce")
    df1["Book checkout"]=df1["Book checkout"].astype(str).str.replace("2063","2023")

    df1[new_col_name]=df1
df1.to_csv("clean_data.csv", index=False)
df2.to_csv("clean_data1.csv", index=False)
