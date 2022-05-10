import pandas as pd
import os

filename = "interview5.txt"
lst = []

# opening file and reading data
with open(filename, "r") as file:
    for line in file:
        lst.append(line.strip().split(","))

data = {}
for i in lst:
    dict_entry_name = i[0]
    dict_entry_list = i
    dict_entry_list.pop(0)
    data[str(dict_entry_name)] = dict_entry_list

# df creation with data dict
interview = pd.DataFrame(data)
interview = interview.rename(index={0: "Value for the customer",
                                    1: "Value for the producer",
                                    2: "Risks for the customer",
                                    3: "Risks for the producer",
                                    4: "Cost of development",
                                    5: "Cost of implementation",
                                    6: "Return of investment",
                                    7: "Market establishment"})

interview_df_current = interview.replace(["l-m", "m-h", "h-m", "m-l", "l-h", "h-l"],
                                         ["l","m","h","m","l","h"])

interview_df_trend = interview.replace(["l-m", "m-h", "h-m", "m-l", "l-h", "h-l"],
                                       ["m", "h", "m", "l", "h", "l"])

# df saved as csv
filename = filename.split(".")[0]
path = os.path.join(os.getcwd(), filename)
if not os.path.isdir(path):
    os.mkdir(path)

baseline_file = os.path.join(path,f"{filename}_baseline.csv")
current_file = os.path.join(path,f"{filename}_current.csv")
trend_file = os.path.join(path,f"{filename}_trend.csv")

if not os.path.exists(baseline_file):
    interview.to_csv(baseline_file)
else:
    print(f"\n{os.path.basename(baseline_file)} already exists.\n")
if not os.path.exists(current_file):
    interview_df_current.to_csv(current_file)
else:
    print(f"{os.path.basename(current_file)} already exists.\n")
if not os.path.exists(trend_file):
    interview_df_trend.to_csv(trend_file)
else:
    print(f"{os.path.basename(trend_file)} already exists.\n")