#MODULE 9: Creating Visualizations in LIS
#author: Logan Grisby
#assignment: use Matplotlib and Seaborn to create and customize plots from a provided dataset of monthly library statistics.





#Step 1) Install required libraries (if not already installed):
##pandas import--
import pandas as pd
##matlab.pyplot import--
import matplotlib.pyplot as plt
##seaborn import--
import seaborn as sns





#Step 2) Load the dataset
try:
  #reads the csv document
  df = pd.read_csv("lis_stats_monthly.csv")
  print("[OK] Dataset loaded successfully.\n")
except FileNotFoundError:
  print("[Error] list_stats_monthly.csv not found. Place in this folder.")
  exit()

# preview data
print(df.head())





#Step 3) Create at least three different types of visualizations using Matplotlib and Seaborn

##Example 1: line plot
##description: line plot of New Library Cards per Month
plt.figure(figsize=(8,4))
plt.plot(df["Month"], df["NewLibraryCards"], marker="o", color="r")
plt.title("Monthly Library Cards")
plt.xlabel("Month")
plt.ylabel("New Library Cards")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


##Example 2: bar chart
##description: bar chart of Programs per Month
plt.figure(figsize=(9,6))
plt.bar(df["Month"], df["Programs"], color="green")
plt.title("Programs per Month")
plt.xlabel("Month")
plt.ylabel("Number of Programs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


##Example 3: scatter plot using Seaborn
##description: scatter plot describing Programs vs. Program Attendance
sns.scatterplot(data=df, x="Programs", y="ProgramAttendance", size="Programs", hue="Programs", palette="coolwarm")

plt.title("Relationship between Programs and Program Attendance")
plt.tight_layout()
plt.show()






#Step 4) Save one visualization
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="Programs", y="ProgramAttendance", size="Programs", hue="Programs", palette="coolwarm")

plt.title("Programs vs. Program Attendance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("program_and_programattendance.png", dpi=300)
print("[OK] Saved plot as program_and_programattendance.png\n")


#Step 5) Write a short reflection describing your process, findings, and challenges
##located in reflection.txt

