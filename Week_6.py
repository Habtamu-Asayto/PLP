#import important libraries
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

#Task 1: Load and Choose a dataset in CSV format (i have created csv file with name, email, phone and age columns)
df = pd.read_csv('dataset.csv')

#Display the csv file.
print(df.head())

#Explore the structure of the dataset by checking the data types and any missing values.
print(df.info())

#Clean the dataset by either filling or dropping any missing values.
df.fillna(method='ffill', inplace=True)   

#Task 2: Data Analysis
#Compute the basic statistics (e.g., mean, median, standard deviation) using .describe().
print(df.describe())

#Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group. the csv file have name email phone and age columns
grouped_data = df.groupby('Phone')['age'].mean().reset_index()
print(grouped_data)

 
#Task 3: Data Visualization
#Line chart showing trends over time (based on age of persons on csv).
plt.figure(figsize=(10, 5))
plt.plot(df['age'], marker='o', linestyle='-', color='b')
plt.title('Age Trends')
plt.xlabel('Index')
plt.ylabel('Age')
plt.grid()
plt.show()

#Bar chart
plt.figure(figsize=(10, 5))
df.groupby('Phone')['age'].mean().plot(kind='bar')
plt.title('Average Age by Phone Number')
plt.xlabel('Phone Number')
plt.ylabel('Average Age')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Histogram 
plt.figure(figsize=(10, 5))
plt.hist(df['age'], bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution')   
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

#Scatter plot 
plt.figure(figsize=(10, 5))
plt.scatter(df['age'], df['Phone'], alpha=0.5, color='orange')
plt.title('Age vs Phone Number')
plt.xlabel('Age')
plt.ylabel('Phone Number')
plt.grid()
plt.show()