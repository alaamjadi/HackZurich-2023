import pickle


def predict_file_content(content):
    # Load model from file
    with open("models/model_v3.pkl", "rb") as f:
        vectorized, model = pickle.load(f)
    text_vec = vectorized.transform([content])
    pred = model.predict(text_vec)[0]
    print(pred)
    if pred == 1:
        return True
    else:
        return False
