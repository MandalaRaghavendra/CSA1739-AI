from sklearn.tree import DecisionTreeClassifier

X = [
    [1, 20],
    [2, 21],
    [3, 22],
    [6, 30],
    [7, 31],
    [8, 32]
]

y = ['No', 'No', 'No', 'Yes', 'Yes', 'Yes']

model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

prediction = model.predict([[7, 30]])

print("Prediction:", prediction[0])
