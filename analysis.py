import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from sklearn.linear_model import LinearRegression


print(os.getcwd())                                                     #checking working directory
print(os.listdir())                                                    #loading file tree
os.chdir("C:/Users/cypherpunk/Desktop/GDG ML OA/T1 Foodborne")         #directory resolution


data=pd.read_csv("outbreaks.csv")                                      #loading the given Kaggle Dataset

#previewing the dataset
print(data.head())
print(data.info())
print(data.describe())


#are foodborne outbreaks increasing or decreasing?
#grouping by 'Year' and taking count (number of outbreaks)
yearly_outbreaks = data.groupby('Year').size()

#checking result of the grouping
print(yearly_outbreaks)

#plotting the trendline
plt.figure(figsize=(10, 6))
plt.plot(yearly_outbreaks.index, yearly_outbreaks.values, marker='o')
plt.title("Trend of Foodborne Disease Outbreaks")
plt.xlabel("Year")
plt.ylabel("Number of Outbreaks")
plt.grid(True)
plt.show()


#fetching unique values from 'Year' column
yearly_outbreaks = data.groupby('Year').size()
print(yearly_outbreaks)

plt.figure(figsize=(10, 6))
plt.plot(yearly_outbreaks.index, yearly_outbreaks.values, marker='o')
plt.title("Trend of Foodborne Disease Outbreaks")
plt.xlabel("Year")
plt.ylabel("Number of Outbreaks")
plt.grid()
plt.show()


#defining: X(Years) and Y(Outbreaks)
X = yearly_outbreaks.index.values.reshape(-1, 1)                        #reshape for sklearn linear regression compatibility
y = yearly_outbreaks.values

#creating and fitting the linear regression model
model = LinearRegression()
model.fit(X, y)

#predicting the Y values (outbreaks) based on the sklearn linear regression model
y_pred = model.predict(X)

#plotting the actual trendline data (scatterplot)
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label="Outbreaks")

#connecting data trendline points for ease of understanding
plt.plot(X, y, color='blue', linestyle='dotted', label="Original Data Line")

#plotting best fit line
plt.plot(X, y_pred, color='red', label="Line of Best Fit")

#labels and title
plt.title("Foodborne Disease Outbreaks with Line of Best Fit")
plt.xlabel("Year")
plt.ylabel("Number of Outbreaks")
plt.grid(True)
plt.legend()
plt.show()


#FOR QUESTION 2: which contaminant most responsible for illnesses, hospitalisations, deaths?
#grouping by the 'Species' and 'Serotype/Genotype' columns, they are definitely the contaminant
contaminant_stats=data.groupby(['Species', 'Serotype/Genotype'])[['Illnesses', 'Hospitalizations', 'Fatalities']].sum()

#printing first few rows to check the result before commiting to approach
print(contaminant_stats.head())

#sorting by illnesses, hospitalizations, and fatalities
most_illnesses=contaminant_stats.sort_values(by='Illnesses', ascending=False).head(1)
most_hospitalizations=contaminant_stats.sort_values(by='Hospitalizations', ascending=False).head(1)
most_fatalities=contaminant_stats.sort_values(by='Fatalities', ascending=False).head(1)

#printing findings
print("Contaminant causing the most illnesses:")
print(most_illnesses)

print("\nContaminant causing the most hospitalizations:")
print(most_hospitalizations)

print("\nContaminant causing the most fatalities:")
print(most_fatalities)

#plotting top 10 contaminants, by illnesses
top_10_contaminants = contaminant_stats.sort_values(by='Illnesses', ascending=False).head(10)

#using bar plot for top 10 species/serotypes
top_10_contaminants[['Illnesses', 'Hospitalizations', 'Fatalities']].plot(kind='bar', figsize=(12, 8))
plt.title("Top 10 Species/Serotypes by Illnesses, Hospitalizations, and Fatalities")
plt.ylabel("Count")
plt.xlabel("Species/Serotype")
plt.xticks(rotation=45)
plt.show()


#further, there can be implicit cues in the dataset that may indicate the presences of particular serotypes in particular food items
#maybe, there is a correlation between them?

#grouping data by 'Food' column (following a theory)
contaminant_stats=data.groupby('Food')[['Illnesses', 'Hospitalizations', 'Fatalities']].sum()

#printing first few rows before I commit to this approach
print(contaminant_stats.head())
#sorting by illnesses, hospitalizations, and fatalities
most_illnesses=contaminant_stats.sort_values(by='Illnesses', ascending=False).head(1)
most_hospitalizations=contaminant_stats.sort_values(by='Hospitalizations', ascending=False).head(1)
most_fatalities=contaminant_stats.sort_values(by='Fatalities', ascending=False).head(1)

#printing results
print("Contaminant causing the most illnesses:")
print(most_illnesses)

print("\nContaminant causing the most hospitalizations:")
print(most_hospitalizations)

print("\nContaminant causing the most fatalities:")
print(most_fatalities)

#plotting top 10 contaminants by illnesses
top_10_contaminants = contaminant_stats.sort_values(by='Illnesses', ascending=False).head(10)

top_10_contaminants[['Illnesses', 'Hospitalizations', 'Fatalities']].plot(kind='bar', figsize=(12, 8))
plt.title("Top 10 Contaminants by Illnesses, Hospitalizations, and Fatalities")
plt.ylabel("Count")
plt.xlabel("Contaminant")
plt.xticks(rotation=45)
plt.show()

#FOR QUESTION 3: what location of food prep poses greatest risk of foodborne sickness?
#grouping by 'Location' and sum(illnesses, hospitalizations, and fatalities)
location_risk = data.groupby('Location')[['Illnesses', 'Hospitalizations', 'Fatalities']].sum()

#sorting by illnesses to find highest-risk locations
location_risk_sorted=location_risk.sort_values(by='Illnesses', ascending=False)

#printing top location causing the most illnesses
print("Location with the greatest risk of foodborne illness (most illnesses):")
print(location_risk_sorted.head(1))

#checking for hospitalizations and fatalities
print("\nLocation with the greatest risk (most hospitalizations):")
print(location_risk.sort_values(by='Hospitalizations', ascending=False).head(1))

print("\nLocation with the greatest risk (most fatalities):")
print(location_risk.sort_values(by='Fatalities', ascending=False).head(1))

#plotting top 10 locations with highest number of illnesses
top_10_locations=location_risk_sorted.head(10)

#using a bar plot
top_10_locations[['Illnesses', 'Hospitalizations', 'Fatalities']].plot(kind='bar', figsize=(12, 8))
plt.title("Top 10 Locations by Illnesses, Hospitalizations, and Fatalities")
plt.ylabel("Count")
plt.xlabel("Location")
plt.xticks(rotation=45)
plt.show()
