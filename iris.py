import numpy as np
import pandas as pd
dataset = pd.read_csv("iris.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
from sklearn.metrics import accuracy_score
print ("Accuracy : ", accuracy_score(y_test, y_pred))
df = pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred})
print(df)
new_test_point = np.array([[6.1,2.9,4.7,1.4]])
prediction = classifier.predict(new_test_point)
print(f"\n Predicted class: {prediction[0]}")


output
     Real Values Predicted Values
0       Iris-setosa      Iris-setosa
1   Iris-versicolor  Iris-versicolor
2       Iris-setosa      Iris-setosa
3    Iris-virginica   Iris-virginica
4       Iris-setosa      Iris-setosa
5       Iris-setosa      Iris-setosa
6    Iris-virginica   Iris-virginica
7       Iris-setosa      Iris-setosa
8       Iris-setosa      Iris-setosa
9    Iris-virginica   Iris-virginica
10  Iris-versicolor  Iris-versicolor
11  Iris-versicolor  Iris-versicolor
12   Iris-virginica   Iris-virginica
13   Iris-virginica   Iris-virginica
14   Iris-virginica   Iris-virginica
15   Iris-virginica   Iris-virginica
16  Iris-versicolor  Iris-versicolor
17  Iris-versicolor  Iris-versicolor
18      Iris-setosa      Iris-setosa
19   Iris-virginica  Iris-versicolor
20  Iris-versicolor  Iris-versicolor
21      Iris-setosa      Iris-setosa
22   Iris-virginica   Iris-virginica
23   Iris-virginica   Iris-virginica
24   Iris-virginica   Iris-virginica
25  Iris-versicolor  Iris-versicolor
26  Iris-versicolor   Iris-virginica
27   Iris-virginica   Iris-virginica
28      Iris-setosa      Iris-setosa
29  Iris-versicolor  Iris-versicolor

 Predicted class: Iris-versicolor
