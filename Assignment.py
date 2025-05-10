import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Task 1: Load and Explore the Dataset
# Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
# Load the dataset using pandas.
# Display the first few rows of the dataset using .head() to inspect the data.
# Explore the structure of the dataset by checking the data types and any missing values.
# Clean the dataset by either filling or dropping any missing values.


#Loading the dataset 
df = pd.read_csv(r"C:\Users\charles.njoroge\Desktop\Codding\Python\week 7.0\Week_7_Assignment.csv")


#Displaying the first few rows

print("First 5 rows of the dataset:")
print(df.head())

#checking data types and missing values

print("\nData types:")
print(df.dtypes)

print("\nMissing values in each column:")
print(df.isnull().sum())

#cleaning the dataset incase any is missing.
# Dropping rows with missing values

df_cleaned = df.dropna()

print("\nDataset after cleaning (if needed):")
print(df_cleaned.head())

#Task 2:

#Computing basic Statistics.

print("Basic Statistics:")
print(df.describe())

#Grouping 
grouped_data = df.groupby('target')['sepal length (cm)'].mean()

print("\nAverage Sepal Length by Species:")
print(grouped_data)

# Patterns Identified:

#  General Statistics:
# Mean Sepal Length: The mean of the sepal length is usually higher for Iris-Versicolor and Iris-Virginica compared to Iris-Setosa. This indicates that Iris-Setosa tends to have smaller sepals overall.

# Petal Length/Width: Iris-Versicolor and Iris-Virginica also tend to have larger petal lengths and widths, with Iris-Virginica having the largest measurements.

# 2. Average Sepal Length by Target (Species):
# Here's an example of how you might summarize the findings based on the target (species):

# plaintext
# Copy code
# Average Sepal Length by Target:
# target
# Iris-Setosa        5.006
# Iris-Versicolor    5.936
# Iris-Virginica     6.588
# Iris-Virginica has the largest average sepal length, followed by Iris-Versicolor, and Iris-Setosa has the smallest average sepal length.

# 3. Correlation Between Features:
# Petal Length vs. Sepal Length: There is a strong positive correlation between petal length and sepal length, especially in the Iris-Virginica and Iris-Versicolor species. The larger the sepal length, the larger the petal length tends to be.

# Petal Width vs. Petal Length: Similarly, petal width and petal length show a strong correlation. Larger petals tend to also have wider widths.

#Task 3.

# Group the data by species and calculate the mean of petal length
mean_petal_length = df.groupby('target')['petal length (cm)'].mean().sort_values()

# Creating the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=mean_petal_length.index, y=mean_petal_length.values, palette='viridis')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.tight_layout()
plt.show()

# This bar chart will show how the petal length varies between the three species in the dataset.
#Creating a Histogram.
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal length (cm)'], kde=True, color='skyblue', bins=15)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#This histogram will show the distribution of the sepal length values in the dataset and include a kernel density estimate (KDE) to visualize the smooth distribution curve.

#Creating a scatter plot for sepatal length vs. petal length.

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='target', palette='Set1')
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species', loc='upper left')
plt.tight_layout()
plt.show()

#In this scatter plot, the points are colored according to the target, which helps to distinguish between the different species based on the relationship between sepal length and petal length.

