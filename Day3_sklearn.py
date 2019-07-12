import pandas as pd
import matplotlib.pyplot as plt

def load_datasets(path):
    # importing datasets
    dataset = pd.read_csv('50_Startups.csv')
    X = dataset.iloc[:, :-1].values
    Y = dataset.iloc[:, 4].values

    # encoding categorial data
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder = LabelEncoder()
    X[:, 3] = labelencoder.fit_transform(X[:, 3])
    onehotencodet = OneHotEncoder(categorical_features=[3])
    X = onehotencodet.fit_transform(X).toarray()


    # avoiding dummy variable trap
    # I don't really understand why there is a dummy variable trap in this dataset. Neither do I understand why removing
    # the first column of the dataset can solve the problem.
    X = X[:, 1:]

    # spliting the datasets into training sets and test sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    # data scaling
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.fit_transform(X_test)

    return X_train, Y_train, X_test, Y_test

X_train, y_train, X_test, y_test = load_datasets('')

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# (y_test, y_pred) should be scattered around the line y_test = y_pred
plt.xlabel('y_test')
plt.ylabel('y_pred')
plt.plot(y_test, y_pred, 'k.')
plt.plot(y_test, y_test, 'g')
plt.show()
