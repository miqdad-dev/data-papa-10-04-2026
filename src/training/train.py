
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.data.loader import load_xy
from src.models.clf import make_model
def train_and_eval(seed: int = 42) -> float:
    X,y = load_xy(); Xtr,Xte,Ytr,Yte = train_test_split(X,y,test_size=0.2,random_state=seed)
    m = make_model(); m.fit(Xtr,Ytr); return accuracy_score(Yte, m.predict(Xte))
if __name__ == '__main__':
    print({'accuracy': train_and_eval()})
