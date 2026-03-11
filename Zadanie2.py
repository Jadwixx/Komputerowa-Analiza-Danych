import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('data2.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length','petal_width'])
#zadanie 2
scaler=MinMaxScaler()
data_scaled=scaler.fit_transform(data)

result = []
saved_centers_scaled = []


for k in range(2,11):
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(data_scaled)
    wcss=kmeans.inertia_
    iterations=kmeans.n_iter_

    result.append({
        'k': k,
        'iterations': iterations,
        'wcss': wcss
    })

    if k==3:
     data['cluster_group']=kmeans.labels_
     saved_centers_scaled=kmeans.cluster_centers_

results_data=pd.DataFrame(result)
print("\n Results")
print(results_data.round(2).to_string())

#zadanie 4
plt.plot(results_data['k'], results_data['wcss'], marker='o', linestyle='-')
plt.title('Wartości WCSS dla każdej wartości k ',fontsize=15)
plt.xlabel('Liczba klastrów (k)', fontsize=11)
plt.ylabel('WCSS', fontsize=11)
plt.xticks(range(2, 11), fontsize=12)
plt.yticks(range(2, 13), fontsize=12)
plt.show()

#zadanie 4
original_centers=scaler.inverse_transform(saved_centers_scaled)
centers_data=pd.DataFrame(original_centers, columns=['sepal_length', 'sepal_width', 'petal_length','petal_width'])

colors_dict = {0:'blue', 1:'orange', 2:'brown'}
colors_list = ['blue', 'orange', 'brown']

fig, ax=plt.subplots(3, 2, figsize=(10,15))

sns.scatterplot(data=data, x='sepal_length', y='sepal_width' , palette=colors_dict, hue='cluster_group', ax=ax[0, 0], legend=False )
ax[0, 0].scatter(centers_data['sepal_length'], centers_data['sepal_width'], c=colors_list, s=100, marker='s', edgecolors='black')
ax[0, 0].set_xlabel('Długość działki kielicha (cm)', fontsize=12)
ax[0, 0].set_ylabel('Szerokość działki kielicha (cm)', fontsize=12)

sns.scatterplot(data=data, x='sepal_length', y='petal_length',  palette=colors_dict, hue='cluster_group', ax=ax[0, 1], legend=False)
ax[0, 1].scatter(centers_data['sepal_length'], centers_data['petal_length'], c=colors_list, s=100, marker='s', edgecolors='black')
ax[0, 1].set_xlabel('Długość działki kielicha (cm)', fontsize=12)
ax[0, 1].set_ylabel('Długość płatka (cm)', fontsize=12)

sns.scatterplot(data=data, x='sepal_length', y='petal_width',  palette=colors_dict, hue='cluster_group', ax=ax[1, 0], legend=False)
ax[1, 0].scatter(centers_data['sepal_length'], centers_data['petal_width'], c=colors_list, s=100, marker='s', edgecolors='black')
ax[1, 0].set_xlabel('Długość działki kielicha (cm)', fontsize=12)
ax[1, 0].set_ylabel('Szerokość płatka (cm)', fontsize=12)

sns.scatterplot(data=data, x='sepal_width', y='petal_length',  palette=colors_dict, hue='cluster_group', ax=ax[1, 1], legend=False)
ax[1, 1].scatter(centers_data['sepal_width'], centers_data['petal_length'], c=colors_list, s=100, marker='s', edgecolors='black')
ax[1, 1].set_xlabel('Szerokość działki kielicha (cm)', fontsize=12)
ax[1, 1].set_ylabel('Długość płatka (cm)', fontsize=12)

sns.scatterplot(data=data, x='sepal_width', y='petal_width',  palette=colors_dict, hue='cluster_group', ax=ax[2, 0], legend=False)
ax[2, 0].scatter(centers_data['sepal_width'], centers_data['petal_width'], c=colors_list, s=100, marker='s', edgecolors='black')
ax[2, 0].set_xlabel('Szerokość działki kielicha (cm)', fontsize=12)
ax[2, 0].set_ylabel('Szerokość płatka (cm)', fontsize=12)

sns.scatterplot(data=data, x='petal_length', y='petal_width',  palette=colors_dict, hue='cluster_group', ax=ax[2, 1], legend=False)
ax[2, 1].scatter(centers_data['petal_length'], centers_data['petal_width'], c=colors_list, s=100, marker='s', edgecolors='black')
ax[2, 1].set_xlabel('Długość płatka (cm)', fontsize=12)
ax[2, 1].set_ylabel('Szerokość płatka (cm)', fontsize=12)

plt.tight_layout()
plt.show()