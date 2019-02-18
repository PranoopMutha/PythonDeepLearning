import pandas as pd
from sklearn.model_selection import train_test_split, RepeatedKFold

df = pd.read_csv('C:\\Users\\MuthaNagaVenkataSaty\\Desktop\\Python DL\\Python Lesson 4\\Python_Lesson6\\iris.csv')
# print(df.head())
# print(df['Species'].unique())
# print(df.describe())


from sklearn.svm import SVC

X = df.as_matrix(
    columns=['sepal length','sepal width','petal length','petal width'])
y = df['Species'].values

#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
kf = RepeatedKFold(n_splits=5, n_repeats=10, random_state=None)
scores=[]
for train_index, test_index in kf.split(X):
      #print("Train:", train_index, "Validation:",test_index)
      X_train, X_test = X[train_index], X[test_index]
      y_train, y_test = y[train_index], y[test_index]

      svm = SVC(kernel="linear")
      svm.fit(X_train, y_train)
      scores.append(svm.score(X_test, y_test))

print(100 * pd.np.mean(scores))