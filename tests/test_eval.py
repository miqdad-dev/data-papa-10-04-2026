
from src.training.train import train_and_eval
def test_accuracy():
    assert train_and_eval() >= 0.85
