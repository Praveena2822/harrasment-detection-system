import joblib
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / 'models' / 'harassment_model.pkl'
VECTORIZER_PATH = BASE_DIR / 'models' / 'tfidf_vectorizer.pkl'
class MLModelService:
    def __init__(self):
        if not MODEL_PATH.exists() or not VECTORIZER_PATH.exists():
            raise FileNotFoundError('Trained model files missing under backend/models/.')
        self.model=joblib.load(MODEL_PATH); self.vectorizer=joblib.load(VECTORIZER_PATH)
    def predict(self,message):
        vector=self.vectorizer.transform([message])
        prediction=int(self.model.predict(vector)[0]); probs=self.model.predict_proba(vector)[0]
        # Avoid assuming the class order in a persisted estimator.
        classes=list(self.model.classes_)
        aggressive_probability=float(probs[classes.index(1)]) if 1 in classes else 0.0
        non_aggressive_probability=float(probs[classes.index(0)]) if 0 in classes else 1.0-aggressive_probability
        return {'prediction':'AGGRESSIVE' if prediction==1 else 'NON-AGGRESSIVE','label':prediction,'aggressive_probability':round(aggressive_probability,3),'non_aggressive_probability':round(non_aggressive_probability,3)}
