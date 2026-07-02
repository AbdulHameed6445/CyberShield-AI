from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def detect_phishing(text):
    result = classifier(text[:512])[0]

    return {
        "label": result["label"],
        "score": round(result["score"] * 100, 2)
    }