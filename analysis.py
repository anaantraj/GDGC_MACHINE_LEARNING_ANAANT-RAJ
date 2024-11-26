import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os


print(os.getcwd())                                                     #checking working directory
print(os.listdir())                                                    #loading file tree
os.chdir("C:/Users/cypherpunk/Desktop/GDG ML OA/T1 Foodborne")         #directory resolution


data=pd.read_csv("outbreaks.csv")                                       #loading the given Kaggle Dataset

#previewing the dataset
print(data.head())
print(data.info())
print(data.describe())


#are foodborne outbreaks increasing or decreasing?
#grouping data by year:
# Group data by year and count outbreaks
"""data['Year'] = pd.to_datetime(data['Year'], errors='coerce').dt.year  # Convert to datetime if needed
yearly_outbreaks = data.groupby('Year').size()

# Plot the trend
plt.figure(figsize=(10, 6))
plt.plot(yearly_outbreaks.index, yearly_outbreaks.values, marker='o')
plt.title("Trend of Foodborne Disease Outbreaks")
plt.xlabel("Year")
plt.ylabel("Number of Outbreaks")
plt.grid()
plt.show()"""
# Check the unique values in the 'Year' column
yearly_outbreaks = data.groupby('Year').size()
print(yearly_outbreaks)

plt.figure(figsize=(10, 6))
plt.plot(yearly_outbreaks.index, yearly_outbreaks.values, marker='o')
plt.title("Trend of Foodborne Disease Outbreaks")
plt.xlabel("Year")
plt.ylabel("Number of Outbreaks")
plt.grid()
plt.show()

