import pickle

# Load sentiment analysis pipeline
with open('./Model/best_sentiment_pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

# Define label mapping
label_mapping = {0: "Negative", 1: "Neutral", 2: "Positive"}


def predict_sentiment(comment):
    prediction = pipeline.predict([comment])[0]
    return label_mapping.get(prediction, "Unknown")


# Extended Test Cases
test_cases = [
    ("I love using Apple Pay, it's so convenient!", "Positive"),
    ("I hate how slow the transaction process is.", "Negative"),
    ("It's okay, but not the best option available.", "Neutral"),
    ("The customer service was fantastic!", "Positive"),
    ("This is the worst experience I've ever had.", "Negative"),
    ("Not bad, but could be better.", "Neutral"),
    ("Absolutely amazing! Highly recommend it.", "Positive"),
    ("I would not recommend this to anyone.", "Negative"),
    ("Meh, it's just alright.", "Neutral"),
    ("Super helpful and easy to use.", "Positive"),
    ("Very frustrating to deal with.", "Negative"),
    ("It's fine, nothing special.", "Neutral"),
    ("Horrible! I'm extremely disappointed.", "Negative"),
    ("Best experience ever!", "Positive"),
    ("It's just okay, neither good nor bad.", "Neutral"),
    ("Ugh, I regret using this service.", "Negative"),
    ("So happy with my purchase!", "Positive"),
    ("Could be worse, could be better.", "Neutral"),
    ("I don't think I'll use this again.", "Negative"),
    ("What a great product!", "Positive")
]

print("\n\033[94mTesting the pipeline with extended comments:\033[0m\n")
for comment, expected in test_cases:
    predicted = predict_sentiment(comment)
    print(f"Comment: {comment}")
    if predicted == expected:
        print(f"Predicted Sentiment: {predicted} (Expected: {expected})")
    else:
        print(f"\033[91mPreficted Sentiment: {predicted} (Expected: {expected} - Incorret)] \033[0m")
    print("-" * 60)

print("\n\033[92m✅ Test cases completed! Review the results above.\033[0m\n")
