from keras.models import Sequential
from keras.layers import Dense
import numpy as np

X = np.array()
y = np.array()

model = Sequential()
model.add(Dense(2, input_shape=(2,)))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=)

model.fit(X, y, epochs=1000)
print(model.predict(X))
