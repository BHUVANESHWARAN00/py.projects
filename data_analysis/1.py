import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1) LOAD DATA
# -----------------------------
csv_path = "annual-enterprise-survey-2024-financial-year-provisional.csv"
df = pd.read_csv(csv_path)

print("=========== HEAD OF DATA ===========")
print(df.head())

print("\n=========== INFO ===========")
print(df.info())

# -----------------------------
# 2) CHECK MISSING VALUES
# -----------------------------
print("\n=========== MISSING VALUES ===========")
print(df.isnull().sum())

# remove rows where Value is missing
df = df.dropna(subset=["Value"])

# -----------------------------
# 3) BASIC STATISTICS
# -----------------------------
print("\n=========== VALUE SUMMARY ===========")
print(df["Value"].describe())

# -----------------------------
# 4) FILTER TOTAL INCOME DATA
# -----------------------------
income_df = df[df["Variable_name"] == "Total income"]

print("\n=========== TOTAL INCOME ROWS ===========")
print(income_df.head())

# -----------------------------
# 5) HIGHEST INCOME INDUSTRY
# -----------------------------
highest_income = income_df.sort_values("Value", ascending=False).head(1)

print("\n=========== HIGHEST INCOME INDUSTRY ===========")
print(highest_income[["Industry_name_NZSIOC", "Value"]])

# -----------------------------
# 6) TOTAL INCOME VS EXPENDITURE
# -----------------------------
total_income = df[df["Variable_name"] == "Total income"]["Value"].sum()
total_expenditure = df[df["Variable_name"] == "Total expenditure"]["Value"].sum()

print("\nTOTAL INCOME:", total_income)
print("TOTAL EXPENDITURE:", total_expenditure)

# -----------------------------
# 7) VISUALIZATION 1
# Top 10 industries by income
# -----------------------------
top10_income = income_df.sort_values("Value", ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top10_income["Industry_name_NZSIOC"], top10_income["Value"])
plt.gca().invert_yaxis()
plt.xlabel("Total Income")
plt.ylabel("Industry")
plt.title("Top 10 Industries by Total Income (2024)")
plt.tight_layout()
plt.show()

# -----------------------------
# 8) VISUALIZATION 2
# Income vs Expenditure
# -----------------------------
labels = ["Total Income", "Total Expenditure"]
values = [total_income, total_expenditure]

plt.figure(figsize=(6,5))
plt.bar(labels, values)
plt.ylabel("Value")
plt.title("Income vs Expenditure (All Industries)")
plt.show()

# -----------------------------
# 9) VISUALIZATION 3
# Category-wise totals
# -----------------------------
category_sum = df.groupby("Variable_category")["Value"].sum()

plt.figure(figsize=(8,5))
plt.bar(category_sum.index, category_sum.values)
plt.xticks(rotation=30)
plt.ylabel("Total Value")
plt.title("Financial Category Totals")
plt.show()

# -----------------------------
# 10) SAVE CLEANED FILE
# -----------------------------
df.to_csv("cleaned_industry_survey_output.csv", index=False)

print("\nCleaned file saved as: cleaned_industry_survey_output.csv")
