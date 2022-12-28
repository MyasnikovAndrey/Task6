import numpy as np
import sys

from main.code.Neural_networks.training_models import models


class PartyNN(object):
    def __init__(self, learning_rate=0.1):
        self.weights_0_1 = np.random.normal(0.0, 2 ** -0.5, (2, 35))
        self.weights_1_2 = np.random.normal(0.0, 1, (1, 2))
        self.sigmoid_mapper = np.vectorize(self.sigmoid)
        self.learning_rate = np.array([learning_rate])

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def predict(self, inputs):
        inputs_1 = np.dot(self.weights_0_1, inputs)
        outputs_1 = self.sigmoid_mapper(inputs_1)

        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.sigmoid_mapper(inputs_2)
        return outputs_2

    def train(self, inputs, expected_predict):
        inputs_1 = np.dot(self.weights_0_1, inputs)
        outputs_1 = self.sigmoid_mapper(inputs_1)

        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.sigmoid_mapper(inputs_2)
        actual_predict = outputs_2[0]

        error_layer_2 = np.array([actual_predict - expected_predict])
        gradient_layer_2 = actual_predict * (1 - actual_predict)
        weights_delta_layer_2 = error_layer_2 * gradient_layer_2
        self.weights_1_2 -= (np.dot(weights_delta_layer_2, outputs_1.reshape(1, len(outputs_1)))) * self.learning_rate

        error_layer_1 = weights_delta_layer_2 * self.weights_1_2
        gradient_layer_1 = outputs_1 * (1 - outputs_1)
        weights_delta_layer_1 = error_layer_1 * gradient_layer_1
        self.weights_0_1 -= np.dot(inputs.reshape(len(inputs), 1), weights_delta_layer_1).T * self.learning_rate

def MSE(y, Y):
    return np.mean((y-Y)**2)

def training():
    #frontend
    train1 = models.front_train()
    # backend
    train2 = models.backend_train()

    train3 = models.train_easy()

    train4 = models.train_qa()

    train5 = models.train_sql()

    train6 = models.train_DataS()

    train7 = models.train_SysAdmin()

    learning_rate = 0.08

    network1 = PartyNN(learning_rate=learning_rate)
    network2 = PartyNN(learning_rate=learning_rate)
    network3 = PartyNN(learning_rate=learning_rate)
    network4 = PartyNN(learning_rate=learning_rate)
    network5 = PartyNN(learning_rate=learning_rate)
    network6 = PartyNN(learning_rate=learning_rate)
    network7 = PartyNN(learning_rate=learning_rate)


    train_and_output(network1, train1)
    train_and_output(network2, train2)
    train_and_output(network3, train3)
    train_and_output(network4, train4)
    train_and_output(network5, train5)
    train_and_output(network6, train6)
    train_and_output(network7, train7)




def train_and_output(network, train):
    epochs = 6000
    learning_rate = 0.08

    for e in range(epochs):
        inputs_ = []
        correct_predictions = []
        for input_stat, correct_predict in train:
            network.train(np.array(input_stat), correct_predict)
            inputs_.append(np.array(input_stat))
            correct_predictions.append(np.array(correct_predict))

        train_loss = MSE(network.predict(np.array(inputs_).T), np.array(correct_predictions))
        sys.stdout.write(
            "\rProgress: {}, Training loss: {}".format(str(100 * e / float(epochs))[:4], str(train_loss)[:5]))

    for input_stat, correct_predict in train:
        print("For input: {} the prediction is: {}, expected: {}".format(
            str(input_stat),
            str(network.predict(np.array(input_stat)) > .5),
            str(correct_predict == 1)))

              # 0 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
    bebra = [([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
    for bebra in bebra:
        print("--------------------------")
        print("For input: {} the prediction is: {}, expected:".format(
            str(bebra),
            str(network.predict(np.array(bebra)) > .5)))
