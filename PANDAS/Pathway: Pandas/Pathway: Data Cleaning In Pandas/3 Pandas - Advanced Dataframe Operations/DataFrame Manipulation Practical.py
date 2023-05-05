import pandas as pd
import numpy as np

df = pd.read_csv("Salaries.csv")

# How many unique jobs are there? Look at the unique method in pandas
job_count = df.pivot_table(columns=['JobTitle'], aggfunc='size')
print(job_count.count())

# Count how many people have the first name "John"
# Case Sensative
johns = df[df["EmployeeName"].str.contains("JOHN")]
print(johns.count())

# Find the surname of everyone whose first name is more than 6 characters long
name_length = df["EmployeeName"].str.split(" ", n=1, expand=True)
df["FirstName"] = name_length[0]
df["LastName"] = name_length[1]
df["NameLength"] = df["FirstName"].str.len()
df_six = df.loc[df["NameLength"] >= 6]
print(df_six["LastName"])

# Create a new column called "last_updated" where every value is equal to the 
# current time (use the datetime 
# module and format the date in ISO format).
df["last_updated"] = pd.Timestamp.now()
df["last_updated"] = pd.to_datetime(df["last_updated"])
print(df["last_updated"])


# Create a new derived column called "time_ratio" in the 
# DataFrame which is the proportion of overtime pay to base pay
df["time_ratio"] = df["OvertimePay"] % df["BasePay"]
print(df["time_ratio"])

# In one line, create a new DataFrame called "new_df" which contains only 
# people who earn more than 100K base salary
new_df = pd.DataFrame(df["BasePay"] >= 100000.00)
print(new_df)

# Now create a new derived column in "new_df" that is the sum of their pays, 
# not including base salary
new_df["Pay"] = df["OvertimePay"] + df["OtherPay"]
print(new_df["Pay"])

# Append a new row to the DataFrame to represent a made up character 
# (Look up the append method in pandas)
# He/she has no benefits, so set this attribute to not a number using np.nan
# Make up the other column values, but make sure they are standardised to 
# the same convention as the other values in that column
new = {"Id": 777, "EmployeeName": "MILLIE JACKSON", "JobTitle": "Software Engineer", "BasePay": 45000.00, "OvertimePay": 0, "OtherPay": 0, "Benifits": np.nan, "TotalPay": 0, "TotalPayBenifits": 0, "Year": 2023, "Agency": "AiCore", "Status": ""}
new_df.append(new, ignore_index=True)
print(new)