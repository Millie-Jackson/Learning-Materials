import pandas as pd

df = pd.read_csv("Salaries.csv")

#job_count = df.pivot_table(columns=['JobTitle'], aggfunc='size')
#print(job_count.count())

# Case Sensative
#johns = df[df["EmployeeName"].str.contains("JOHN")]
#print(johns.count())

#name_length = df["EmployeeName"].str.split(" ", n=1, expand=True)
#df["FirstName"] = name_length[0]
#df["LastName"] = name_length[1]
#df["NameLength"] = df["FirstName"].str.len()
#df_six = df.loc[df["NameLength"] >= 6]
#print(df_six["LastName"])

df["last_updated"] = pd.Timestamp.now()
df["last_updated"] = pd.to_datetime(df["last_updated"])
print(df["last_updated"])