import os
import pandas as pd


df = pd.DataFrame.from_csv("train.csv")

print(df.head())
print("train shape", df.shape)

dir_name = "10images"

images = os.listdir(dir_name)

segments_df = df.loc[images]

print(dir_name, "shape", segments_df.shape)

segments_df.to_csv(f"{dir_name}.csv")