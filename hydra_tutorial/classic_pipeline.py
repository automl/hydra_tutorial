import warnings

import hydra
import numpy as np
from omegaconf import DictConfig
from sklearn import datasets
from sklearn.exceptions import ConvergenceWarning
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neural_network import MLPClassifier

from hydra_tutorial.utils import dump_logs

warnings.filterwarnings("ignore", category=ConvergenceWarning)

# We load the digits dataset
digits = datasets.load_digits()
X, y = digits.data, digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


@hydra.main(version_base=None, config_path="configs", config_name="base")
def train_mlp(cfg: DictConfig) -> float:
    warnings.filterwarnings("ignore", category=ConvergenceWarning)

    # we want to have reproducible training
    np.random.seed(seed=cfg.seed)

    # for illustrative purposes, you can reduce max_iter drastically here
    classifier = MLPClassifier(
        hidden_layer_sizes=cfg.hidden_layer_sizes,
        max_iter=cfg.max_iter,
        activation=cfg.activation,
        solver=cfg.solver,
        alpha=cfg.alpha,
    )
    scores = cross_val_score(classifier, X_train, y_train, cv=5)

    mean_score = np.mean(scores)

    print(f"Mean accuracy: {mean_score:.4f}")

    # Let's produce a log file
    dump_logs(log_data={"mean_acc": mean_score}, filename="performance.jsonl")

    return 1 - mean_score  # mean accuracy over folds


if __name__ == "__main__":
    train_mlp()
