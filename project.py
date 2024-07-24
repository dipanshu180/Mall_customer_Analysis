import pandas as pa 
import  matplotlib.pyplot as pot
import seaborn as sc
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


file_path = 'Mall_Customers.csv'
data = pa.read_csv(file_path)

data.columns=['ID','Gender','Age','AnualIncome','SpendingScore'] 
count = data.isnull().sum()
print(count)

data['Gender'] = data['Gender'].map({'Male':0 , 'Female':1})
print(data.head(10))
print(data.describe())


#histplot-age ,Anual income, Spending Score
# Visualisation Distribution
fig, axs = pot.subplots(2, 2, figsize=(20, 12))

sc.histplot(data['Age'], bins =30 ,kde=True,ax=axs[0,0]) 
axs[0,0].set_title('Age Distributiom')


sc.histplot(data['AnualIncome'],bins =30 , kde=True,ax =axs[0,1])
axs[0,1].set_title('Income Distribution')
 

sc.histplot(data['SpendingScore'],bins=30,kde=True ,ax =axs[1,0])
axs[1,0].set_title('SpendingScore')


sc.scatterplot(data=data , x='AnualIncome',y='SpendingScore',hue='Gender',ax =axs[1,1])
axs[1,1].set_title('Income vs Spending score')


pot.tight_layout
pot.show()


# Feature selection
features = data[['Age', 'AnualIncome', 'SpendingScore']]

# Standardizing the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Applying K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(scaled_features)

# Evaluating cluster quality
pot.figure(figsize=(10, 6))
sc.scatterplot(data=data, x='AnualIncome', y='SpendingScore', hue='Cluster', palette='viridis')
pot.title('Customer Segments')
pot.show()