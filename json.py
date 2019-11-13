import json
import pandas as pd

with open('bayes.json') as f:
    bayes = json.load(f)

location = bayes['Location']
floor = bayes['Floor']
print(f'The class is in the {location} room on the {floor}th floor.')

if bayes['isActive']:
    print('Bayes is active.')

n_students = len(bayes['Students'])
n_instructors = len(bayes['Instructors'])
print(f'Number of instructors: {n_instructors}')
print(f'Number of students: {n_students}')

max_lang = 0
corr_instructor = None
for instructor in bayes['Instructors']:
    if len(instructor['favoriteLanguages']) > max_lang:
        max_lang = len(instructor['favoriteLanguages'])
        corr_instructor = instructor['name']
    
print(corr_instructor)

students = pd.DataFrame(bayes['Students'])
# each dictionary key becomes the title of a column, even if its value isn't a simple datatype (e.g. list)