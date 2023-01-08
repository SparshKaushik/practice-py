from sklearn.linear_model import LinearRegression
X = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
model = LinearRegression()
model.fit(X, y)
X_test = [[20, 2], [70, 4]]
y_pred = model.predict(X_test)
print(f"Predicted values: {y_pred}")
