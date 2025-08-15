from sentence_transformers import SentenceTransformer
import joblib

# Load the sentence transformer model
transformer_model = SentenceTransformer('all-MiniLM-L6-v2')
# Load the saved classifier
classifier_model = joblib.load('training/models/log_classifier.joblib')

# code to classify log_message using saved model (models/log_classifier) and sentence transformer embedding
def classify_with_bert(log_message):

    # Generate embedding for the input log_message
    message_embedding = transformer_model.encode([log_message])
    probabilities = classifier_model.predict_proba(message_embedding)[0]
    if max(probabilities)< 0.5:
        return "unclassified"
    # Predict the class
    prediction_label = classifier_model.predict(message_embedding)[0]
    return prediction_label




if __name__ == "__main__":
    logs = [
        "nova.osapi_compute.wsgi.server [req-86b60c9f-5825-4447-9b26-c90aa4eb5986 113d3a99c3da401fbd62cc2caa5b96d2 54fadb412c4e40cdbaed9335e4c35a9e - - -] 10.11.10.1 GET /v2/54fadb412c4e40cdbaed9335e4c35a9e/servers/detail HTTP/1.1 Status code -  200 len: 1759 time: 0.2631650",
        "Data replication task for shard 14 did not complete",
        "User User395 logged in.",
        "Multiple login failures occurred on user 9052 account",
        "hey bro, chill"
    ]
    for log in logs:
        label = classify_with_bert(log)
        print(label)