import pandas
import sys

print('\nPython version ' + sys.version)
print('Pandas version ' + pandas.__version__)

data = pandas.read_csv('titanic.csv', index_col='PassengerId')

# Question 1
print("\nQuestion 1. Passenger count by sex:")
print(data['Sex'].value_counts())

# Question 2
print("\nQuestion 2. Passenger survived part:")
print(data['Survived'].value_counts())
# print(round((data['Survived'].value_counts(normalize=True)[:1]*100), 2))
print(round((data['Survived'].value_counts(normalize=True)*100), 2))

# Question 3
print("\nQuestion 3. 1 st class part:")
print(round((data['Pclass'].value_counts(normalize=True, sort=False)[:1]*100), 2))

# Question 4
print("\nQuestion 4. Passengers age:")
print(round(data['Age'].mean(), 2))
print(round(data['Age'].median(), 2))

# Question 5
print("\nQuestion 5. Pearson corr:")
print(round(data['SibSp'].corr(data['Parch']), 2))

# Question 6
print("\nQuestion 6. Most popular woman first name:")
woman = data.loc[data['Sex'] == 'female']
s1 = woman['Name']\
    .str.split(' ', expand=True).stack()\
    .str.strip()\
    .str.replace('(', '')\
    .str.replace(')', '')\
    .str.replace('.', '')\
    .str.replace(',', '')\
    .reset_index(level=1, drop=True)
print(s1.value_counts())
