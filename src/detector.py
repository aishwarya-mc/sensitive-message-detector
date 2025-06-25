import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# LoadING the AI model and vectorizer
def load_model():
    with open(r'models\sensitive_message_detector_model.pkl.txt', 'rb') as model_file:
        model = pickle.load(model_file)
    with open(r'models\vectorizer.pkl.txt', 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)
    return model, vectorizer

def detect_sensitivity(message):
    model, vectorizer = load_model()
    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)
    
    if prediction[0] == 'Sensitive':
        return True  # Sensitive message
    return False  # Non-sensitive message
