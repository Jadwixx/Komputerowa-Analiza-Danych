import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#odczytanie danych z pliku csv
data=pd.read_csv('data1.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length','petal_width','species'])
print(data)

#zadanie 1
print("The data are presented with an accuracy of one decimal place.")
#liczebność po gatunku
numberOfSpecimens=data['species'].value_counts()
print(numberOfSpecimens.to_string())
#udziały procentowe
percentage_shares=numberOfSpecimens/numberOfSpecimens.sum()*100
print(percentage_shares.round(1).to_string())
print(numberOfSpecimens.sum(), percentage_shares.sum().round(1), '\n')


#zadanie 2
print("The data are presented with an accuracy of two decimal places.")

print('Sepal_length:',
      '\nminimum: ', np.min(data['sepal_length']).round(2),
      '\nmaximum: ', np.max(data['sepal_length']).round(2),
      '\nmedian: ', np.median(data['sepal_length']).round(2),
      '\nquantileQ1: ', np.quantile(data['sepal_length'], 0.25).round(2),
      '\nquantileQ3: ', np.quantile(data['sepal_length'], 0.75).round(2),
      '\naverage: ', np.average(data['sepal_length']).round(2),
      '\nstandard_deviation: ', np.std(data['sepal_length'],ddof=1).round(2),'\n'
      #ddof - poprawka stopni swobody -> aby odchylenie standardowe było liczone dla próby N-1 w mianowniku wzoru.
     )

print('Sepal_width:',
      '\nminimum: ', np.min(data['sepal_width']).round(2),
      '\nmaximum: ', np.max(data['sepal_width']).round(2),
      '\nmedian: ', np.median(data['sepal_width']).round(2),
      '\nquantileQ1: ', np.quantile(data['sepal_width'], 0.25).round(2),
      '\nquantileQ3: ', np.quantile(data['sepal_width'], 0.75).round(2),
      '\naverage: ', np.average(data['sepal_width']).round(2),
      '\nstandard_deviation: ', np.std(data['sepal_width'],ddof=1).round(2),'\n'
     )

print('Petal_length:',
      '\nminimum: ', np.min(data['petal_length']).round(2),
      '\nmaximum: ', np.max(data['petal_length']).round(2),
      '\nmedian: ', np.median(data['petal_length']).round(2),
      '\nquantileQ1: ', np.quantile(data['petal_length'], 0.25).round(2),
      '\nquantileQ3: ', np.quantile(data['petal_length'], 0.75).round(2),
      '\naverage: ', np.average(data['petal_length']).round(2),
      '\nstandard_deviation: ', np.std(data['petal_length'],ddof=1).round(2),'\n'
     )

print('Petal_width:',
      '\nminimum: ', np.min(data['petal_width']).round(2),
      '\nmaximum: ', np.max(data['petal_width']).round(2),
      '\nmedian: ', np.median(data['petal_width']).round(2),
      '\nquantileQ1: ', np.quantile(data['petal_width'], 0.25).round(2),
      '\nquantileQ3: ', np.quantile(data['petal_width'], 0.75).round(2),
      '\naverage: ', np.average(data['petal_width']).round(2),
      '\nstandard_deviation: ', np.std(data['petal_width'],ddof=1).round(2),'\n'
     )

#zadanie 3
fig, ax = plt.subplots(4, 2, figsize=(9,12))


sns.histplot(data, x='sepal_length', bins=np.arange(4., 8.5, .5), ax=ax[0, 0])
ax[0, 0].set_title('Długość działki kielicha', fontsize=22)
ax[0, 0].set_xlabel('Długość (cm)', fontsize=14)
ax[0, 0].set_ylabel('Liczebność', fontsize=14)
ax[1, 0].set_yticks(np.arange(0, 36, 5))
ax[0, 0].set_ylim(top=35)
ax[0, 0].tick_params(labelsize=11)


sns.boxplot(data, x='species', y='sepal_length', ax=ax[0, 1], medianprops={'color': 'red'}, color='white',
        linecolor='black', widths=0.4)
ax[0, 1].set_xlabel('Gatunek', fontsize=14)
ax[0, 1].set_ylabel('Długość (cm)', fontsize=14)
ax[0, 1].set_yticks(np.arange(4., 8.5, .5))
ax[0, 1].set_ylim(4.0, 8.0)
ax[0, 1].set_xticks([0, 1, 2], labels=['setosa', 'versicolor', 'virginica'])
ax[0, 1].tick_params(labelsize=11)



sns.histplot(data, x='sepal_width', bins=np.arange(2., 5., .5), ax=ax[1, 0],)
ax[1, 0].set_title('Szerokość działki kielicha', fontsize=22)
ax[1, 0].set_xlabel('Szerokość(cm)', fontsize=14)
ax[1, 0].set_ylabel('Liczebność', fontsize=14)
ax[1, 0].set_yticks(np.arange(0, 81, 10))
ax[1, 0].set_ylim(top=80)
ax[1, 0].tick_params(labelsize=11)


sns.boxplot(data, x='species', y='sepal_width', ax=ax[1, 1], medianprops={'color': 'red'}, color='white',
            linecolor='black', widths=0.4)
ax[1, 1].set_xlabel('Gatunek', fontsize=14)
ax[1, 1].set_ylabel('Szerokość (cm)', fontsize=14)
ax[1, 1].set_yticks(np.arange(0., 5.5, .5))
ax[1, 1].set_ylim(0.0, 5.0)
ax[1, 1].set_xticks([0, 1, 2], labels=['setosa', 'versicolor', 'virginica'])
ax[1, 1].tick_params(labelsize=11)


sns.histplot(data, x='petal_length', bins=np.arange(1.0, 7.5, .5), ax=ax[2, 0])
ax[2, 0].set_title('Długość płatka', fontsize=22)
ax[2, 0].set_xlabel('Długość(cm)', fontsize=14)
ax[2, 0].set_ylabel('Liczebność', fontsize=14)
ax[2, 0].set_yticks(np.arange(0., 31, 5))
ax[2, 0].set_ylim(top=30)
ax[2, 0].tick_params(labelsize=11)

sns.boxplot(data, x='species', y='petal_length', ax=ax[2, 1], medianprops={'color': 'red'},color='white',
            linecolor='black', widths=0.4)
ax[2, 1].set_xlabel('Gatunek', fontsize=14)
ax[2, 1].set_ylabel('Długość (cm)', fontsize=14)
ax[2, 1].set_yticks(np.arange(0., 8.5, 1.))
ax[2, 1].set_ylim(0.0, 8.0)
ax[2, 1].set_xticks([0, 1, 2], labels=['setosa', 'versicolor', 'virginica'])
ax[2, 1].set_xticks([0, 1, 2], labels=['setosa', 'versicolor', 'virginica'])
ax[2, 1].tick_params(labelsize=11)


sns.histplot(data, x='petal_width', bins=np.arange(0.0, 3.0, .5), ax=ax[3, 0])
ax[3, 0].set_title('Szerokość płatka', fontsize=22)
ax[3, 0].set_xlabel('Szerokość(cm)', fontsize=14)
ax[3, 0].set_ylabel('Liczebność', fontsize=14)
ax[3, 0].set_yticks(np.arange(0., 61, 10))
ax[3, 0].set_ylim(top=60)
ax[3, 0].tick_params(labelsize=11)

sns.boxplot(data, x='species', y='petal_width', ax=ax[3, 1], medianprops={'color': 'red'}, color='white',
            linecolor='black', widths=0.4)
ax[3, 1].set_xlabel('Gatunek', fontsize=14)
ax[3, 1].set_ylabel('Szerokość(cm)', fontsize=14)
ax[3, 1].set_yticks(np.arange(0.0, 2.7, 0.5))
ax[3, 1].set_ylim(0.0, 2.6)
ax[3, 1].set_xticks([0, 1, 2], labels=['setosa', 'versicolor', 'virginica'])
ax[3, 1].tick_params(labelsize=11)
#aby nie nachodziły labels na siebie
plt.tight_layout()
plt.show()

#zadanie 4
def calculate_ols_regression(x: pd.Series, y: pd.Series) -> dict:
    r = x.corr(y)
    numerator_a = np.sum((x - np.average(x)) * (y - np.average(y)))
    denominator_a = np.sum((x - np.average(x)) ** 2)
    a = numerator_a / denominator_a
    b = np.average(y) - a * np.average(x)
    regression_line = a * x + b

    if b < 0:
        label_text = f'r = {r:.2f}; y = {a:.1f}x - {abs(b):.1f}'
    else:
        label_text = f'r = {r:.2f}; y = {a:.1f}x + {b:.1f}'

    return {
        'r': r,
        'a': a,
        'b': b,
        'regression_line': regression_line,
        'label_text': label_text
    }


fig, ax = plt.subplots(3, 2, figsize=(9, 12))


x=data["sepal_length"]
y=data["sepal_width"]

result = calculate_ols_regression(x, y)


sns.scatterplot(x=x, y=y, ax=ax[0,0], s=80, edgecolor='none')
ax[0,0].set_title(result["label_text"], fontsize=20)
ax[0,0].plot(x, result["regression_line"], color='red')
ax[0,0].set_xticks(np.arange(4, 9, 1))
ax[0,0].set_xlim(4, 8)
ax[0,0].set_xlabel('Długość działki kielicha (cm)', fontsize=14)
ax[0,0].set_ylabel('Szerokość działki kielicha (cm)', fontsize=12)


x=data["sepal_length"]
y=data["petal_length"]

result = calculate_ols_regression(x, y)

sns.scatterplot(x=x, y=y, ax=ax[0, 1], s=80, edgecolor='none')
ax[0,1].set_title(result["label_text"], fontsize=20)
ax[0,1].plot(x, result["regression_line"], color='red')
ax[0,1].set_xticks(np.arange(4, 9, 1))
ax[0,1].set_xlim(4, 8)
ax[0,1].set_xlabel('Długość działki kielicha (cm)', fontsize=14)
ax[0,1].set_ylabel('Długość płatka (cm)', fontsize=12)


x=data["sepal_length"]
y=data["petal_width"]

result = calculate_ols_regression(x, y)

sns.scatterplot(x=x, y=y, ax=ax[1, 0], s=80, edgecolor='none')
ax[1,0].set_title(result["label_text"], fontsize=20)
ax[1,0].plot(x, result["regression_line"], color='red')
ax[1,0].set_xticks(np.arange(4, 9, 1))
ax[1,0].set_xlim(4, 8)
ax[1,0].set_xlabel('Długość działki kielicha (cm)', fontsize=14)
ax[1,0].set_ylabel('Szerokość płatka (cm)', fontsize=12)


x=data["sepal_width"]
y=data["petal_length"]

result = calculate_ols_regression(x, y)

sns.scatterplot(x=x, y=y, ax=ax[1, 1], s=80, edgecolor='none')
ax[1,1].set_title(result["label_text"], fontsize=20)
ax[1,1].plot(x, result["regression_line"], color='red')
ax[1,1].set_xticks(np.arange(1, 6, 1))
ax[1,1].set_xlim(1, 5)
ax[1,1].set_xlabel('Szerokość działki kielicha (cm)', fontsize=14)
ax[1,1].set_ylabel('Długość płatka (cm)', fontsize=12)


x=data["sepal_width"]
y=data["petal_width"]

result = calculate_ols_regression(x, y)

sns.scatterplot(x=x, y=y, ax=ax[2, 0], s=80, edgecolor='none')
ax[2,0].set_title(result["label_text"], fontsize=20)
ax[2,0].plot(x, result["regression_line"], color='red')
ax[2,0].set_xticks(np.arange(0, 6, 1))
ax[2,0].set_xlim(1, 6)
ax[2,0].set_xlabel('Szerokość działki kielicha (cm)', fontsize=14)
ax[2,0].set_ylabel('Szerokość płatka (cm)', fontsize=12)


x=data["petal_length"]
y=data["petal_width"]

result = calculate_ols_regression(x, y)

sns.scatterplot(x=x, y=y, ax=ax[2, 1], s=80, edgecolor='none')
ax[2,1].set_title(result["label_text"], fontsize=20)
ax[2,1].plot(x, result["regression_line"], color='red')
ax[2,1].set_xticks(np.arange(0, 9, 1))
ax[2,1].set_xlim(0, 8)
ax[2,1].set_xlabel('Długość płatka (cm)', fontsize=14)
ax[2,1].set_ylabel('Szerokość płatka (cm)', fontsize=12)
plt.tight_layout()
plt.show()