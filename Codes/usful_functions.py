import pandas as pd
import numpy as np


def change_col_year_to_index(inp_df: pd.DataFrame, index_col: list) -> pd.DataFrame:
    df_index = inp_df[index_col].copy()
    res_df = pd.DataFrame()
    for col in inp_df.columns:
        if col not in df_index.columns:
            year = int(col)
            new_df = df_index.copy()
            new_df["Year"] = year
            new_df["value"] = inp_df[col]
            res_df = pd.concat([res_df, new_df], ignore_index=True)
    return res_df

