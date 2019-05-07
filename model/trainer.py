from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

if __name__=='__main__':
    df = pd.read_csv('dataset/processed.csv')
    df = df.drop(['reading score', 'writing score'],axis=1)

    X = df.drop(['math score'], axis=1)
    y = df['math score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33)

    model = SVC(gamma='auto' ,kernel='rbf')
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    print(accuracy_score(y_test, y_pred))

