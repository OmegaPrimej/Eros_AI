import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class NeuralNetwork:
    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_shape=(10,)))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(10, activation='softmax'))
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=)
