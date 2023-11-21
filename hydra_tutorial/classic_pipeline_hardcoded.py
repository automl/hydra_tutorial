from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.exceptions import ConvergenceWarning
import warnings

warnings.filterwarnings("ignore", category=ConvergenceWarning)

# We load the digits dataset
digits = datasets.load_digits()
X, y = digits.data, digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


def train_mlp() -> float:
    # we want to have reproducible training
    np.random.seed(seed=1234)

    # for illustrative purposes, you can reduce max_iter drastically here
    classifier = MLPClassifier(hidden_layer_sizes=(100,), max_iter=100, activation="relu", solver="adam")
    scores = cross_val_score(classifier, X_train, y_train, cv=5)

    return np.mean(scores)  # mean accuracy over folds


if __name__ == "__main__":
    # Ignore the warnings for now:)
    cv_loss = train_mlp()
    print(f"Cross_validation accuaracy on digits {cv_loss}")
