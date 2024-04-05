import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(PROJECT_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, "data")
TEST_DIR = os.path.join(PROJECT_DIR, "tests")
DATA_MNIST_FULL = os.path.join(DATA_DIR, "mnist_full")
DATA_MNIST_SMALL = os.path.join(DATA_DIR, "mnist_small")

NUM_DIGIT = 10
TRAINING = "training"
TESTING = "testing"