from flask import Flask, render_template, request
import pickle

from utils.preprocessing import transform_text

app = Flask(__name__)

# Load model and vectorizer
tfidf = pickle.load(open("model/vectorizer.pkl", "rb"))
model = pickle.load(open("model/model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    message = request.form["message"].strip()

    # Empty input validation
    if message == "":
        return render_template(
            "index.html",
            prediction="Please enter a message.",
            confidence=""
        )

    # Preprocess
    transformed = transform_text(message)

    # Vectorize
    vector = tfidf.transform([transformed])

    # Prediction
    prediction = model.predict(vector)[0]

    # Confidence
    probability = model.predict_proba(vector).max() * 100

    result = "Spam 🚨" if prediction == 1 else "Ham ✅"

    return render_template(
        "index.html",
        prediction=result,
        confidence=f"{probability:.2f}",
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)