
from sklearn.datasets import load_iris as sk_load_iris
def load_xy():
    return sk_load_iris(return_X_y=True)
