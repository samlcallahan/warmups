from pydataset import data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

vote = data('voteincome')

vote = vote.drop(columns=['state', 'year'])

train, test = train_test_split(vote)

y_train = train[['vote']]
x_train = train.drop(columns=['vote'])

y_test = test[['vote']]
x_test = test.drop(columns=['vote'])

knn = KNeighborsClassifier(n_neighbors=4)

knn.fit(x_train, y_train)

y_train['predicted'] = knn.predict(x_train)
y_test['predicted'] = knn.predict(x_test)

train_accuracy = (y_train.predicted == y_train.vote).mean() # 90%
test_accuracy = (y_test.predicted == y_test.vote).mean() # 79%

for i in range(1,5):
    y_train.drop(columns='predicted', inplace=True)

    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train, y_train)

    y_train['predicted'] = knn.predict(x_train)
    y_test['predicted'] = knn.predict(x_test)

    train_accuracy = (y_train.predicted == y_train.vote).mean()
    test_accuracy = (y_test.predicted == y_test.vote).mean() 
    print(f'Train accuracy: {train_accuracy}')
    print(f'Test accuracy: {test_accuracy}')

# It works best at k=1, train accuracy of 98%, test accuracy of 86%

y_train.drop(columns='predicted', inplace=True)

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(x_train, y_train)

y_train['predicted'] = knn.predict(x_train)
y_test['predicted'] = knn.predict(x_test)

y = pd.concat([y_train, y_test])

print(classification_report(y['vote'], y['predicted']))

# accuracy is what % of voters we correctly predicted to vote/not
# precision is what % of our predictions were correct (e.g. if we predicted 600 voters would vote, what % of them would actually vote)
# recall is what % of results we accurately predicted (e.g. if 600 people voted, what % of them did we accurately label)