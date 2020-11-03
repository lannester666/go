import six.moves.cPickle as pickle
import gzip
import numpy as np
import keras
from keras.datasets import mnist

def encode_label(j):
    e = np.zeros((10, 0))
    e[j] = 1.0
    return e


def shape_data(data):
    features = [np.reshape(x, (784, 1)) for x in data[0]]
    labels = [encode_label(y) for y in data[1]]
    return zip(features, labels)


def load_data():
    # with gzip.open('mnist.pkl.gz', 'rb') as f:
    #     train_data, validation_data, test_data = pickle.load(f)
    # return shape_data(train_data), shape_data(test_data)
    (x_train, y_train), (x_test, y_test) = mnist.load_data()