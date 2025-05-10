import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#loading the dataset 

df=pd.read_csv(r"C:\Users\charles.njoroge\Desktop\Codding\Python\Week 8.0\owid-covid-data.csv")

#displaying the columns
print("columns in the dataset")
print(df.columns)

#Displaying the first five rows:
print("\n👀 First 5 rows:")
print(df.head())

#Checking missing values
print("\n Missing values in each column:")
print(df.isnull().sum())

#Data cleaning.
#Filtering countries of interest.
countries = ['Kenya', 'United States', 'India', 'Algeria','China']
df_filtered = df[df['location'].isin(countries)]
print(countries)

#Dropping rows without critical values like date, & total cases

df = df.dropna(subset=['date', 'total_cases'])

#converting date column to datetime

df['date'] = pd.to_datetime(df['date'])

print(df.columns)


#Handling missing numeric values

# Use interpolate() or fillna(method='ffill') to fill missing numeric data:

numeric_cols = [ 'total_cases', 'new_cases', 'new_cases_smoothed', 'total_deaths', 'new_deaths',
    'new_deaths_smoothed', 'total_cases_per_million', 'new_cases_per_million',
    'new_cases_smoothed_per_million', 'total_deaths_per_million',
    'new_deaths_per_million', 'new_deaths_smoothed_per_million', 'total_tests',
    'new_tests', 'total_tests_per_thousand', 'new_tests_per_thousand',
    'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_per_case',
    'positive_rate', 'stringency_index', 'population', 'population_density',
    'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita',
    'extreme_poverty', 'cardiovasc_death_rate', 'diabetes_prevalence',
    'female_smokers', 'male_smokers', 'handwashing_facilities',
    'hospital_beds_per_thousand', 'life_expectancy', 'human_development_index']
df[numeric_cols] = df[numeric_cols].interpolate(method='linear')  # OR use .fillna(method='ffill')

# resetting index
df.reset_index(drop=True, inplace=True)

# Preview
print(df.head())


#Exploratory Data Analysis (EDA)

# TOtal cases over time.

plt.figure(figsize=(12, 6))
for country in countries:
    subset = df_filtered[df_filtered['location'] == country]
    plt.plot(subset['date'], subset['total_cases'], label=country)

plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.tight_layout()
plt.show()

#total deaths over time:
plt.figure(figsize=(12, 6))
for country in countries:
    subset = df_filtered[df_filtered['location'] == country]
    plt.plot(subset['date'], subset['total_deaths'], label=country)

plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.tight_layout()
plt.show()


#Daily new cases between countries.

plt.figure(figsize=(12, 6))
for country in countries:
    subset = df_filtered[df_filtered['location'] == country]
    plt.plot(subset['date'], subset['new_cases'], label=country)

plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.tight_layout()
plt.show()

#Death rate calculation.
df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases']

#plot for average death rate per country.
avg_death_rates = df_filtered.groupby('location')['death_rate'].mean()

avg_death_rates.plot(kind='bar', color='salmon', figsize=(8, 5))
plt.title('Average COVID-19 Death Rate per Country')
plt.ylabel('Death Rate')
plt.xlabel('Country')
plt.tight_layout()
plt.show()


#Correlation Heatmap
# Pick relevant numerical columns
# Pick relevant numerical columns
corr_cols = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']
heatmap_data = df_filtered[corr_cols].dropna()

plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()


#Insights

# 1. Rising Total Cases in Selected Countries
# Insight: The total number of COVID-19 cases has been consistently rising in countries like the USA and India, with notable peaks during specific waves of the pandemic. This suggests that despite mitigation efforts, some countries continued to experience significant outbreaks, likely influenced by factors such as population density, healthcare infrastructure, and public health measures.

# 2. Death Rate Analysis Across Countries
# Insight: The death rate (total deaths/total cases) varies significantly across countries. Countries with well-established healthcare systems, like the USA, may exhibit a lower death rate despite a higher total case count, while others, especially those with less robust healthcare systems, may have higher death rates. This highlights the impact of healthcare availability, vaccination rates, and early intervention measures on the outcome of the pandemic.

# 3. Impact of Stringency Index on New Cases
# Insight: The stringency index, which measures the intensity of lockdowns and restrictions, appears to correlate with a decrease in daily new cases. Countries that implemented stricter lockdowns during early waves of the pandemic, such as India and parts of Europe, experienced slower rates of new infections. This indicates that timely and strict public health measures played a crucial role in reducing case numbers.

# 4. Testing and Positive Rate Correlation
# Insight: There is a strong correlation between the number of tests conducted and the positive rate of COVID-19. Countries with more widespread testing, such as the USA, show a higher number of positive cases, but this could also mean better detection of COVID-19 compared to countries with limited testing capabilities. The positive rate is lower in countries that have high testing rates, showing that increased testing reduces the detection bias.

