import pickle


def predict_file_content(content):
    # Load model from file
    with open("model_v2.pkl", "rb") as f:
        vectorized, model = pickle.load(f)
    text_vec = vectorized.transform([content])
    if model.predict(text_vec)[0] == 1:
        return True
    else:
        return False


