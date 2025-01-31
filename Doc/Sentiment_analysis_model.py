from sklearn.base import clone
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score, precision_score
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
import pandas as pd
import pickle
import re
from langdetect import detect
from nltk.tokenize import word_tokenize

# nltk.download("punkt")

# Load dataset
df = pd.read_csv(
    "./data/YoutubeCommentsDataSet.csv").fillna("")

# Load multilingual stopwords
try:
    stopwords = pd.read_csv("./data/stopwords.csv")
    stopword_dict = {lang: set(words.split(","))
                     for lang, words in stopwords.values}
except:
    stopword_dict = {"en": set()}

# Detect language
def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

# Preprocess text
def preprocess_text(text):
    text = re.sub(
        r"http\S+|www\S+|@\S+|#\S+|[^a-zA-Z0-9\s]", "", text.lower().strip())
    words = word_tokenize(text)
    stop_words = stopword_dict.get(detect_language(text), set())
    return " ".join([word for word in words if word not in stop_words])


# Apply preprocessing
df["Processed_Comment"] = df["Comment"].apply(preprocess_text)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(
    max_features=15000, ngram_range=(1, 3), max_df=0.85, min_df=5)
X = vectorizer.fit_transform(df["Processed_Comment"])

# Encode labels
y = LabelEncoder().fit_transform(df["Sentiment"])

# Handle class imbalance
X, y = SMOTE(random_state=42).fit_resample(X, y)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)

# Models to compare
models = {
    "Random Forest": RandomForestClassifier(n_estimators=200, max_depth=20, random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=1000, C=1.0, random_state=42),
    "Naive Bayes": MultinomialNB(),
    "SVM": SVC(kernel='linear', probability=True, random_state=42),
    "XGBoost": XGBClassifier(eval_metric='mlogloss', max_depth=10, random_state=42)
}

best_model, best_precision, best_model_name = None, 0, ""

# Train and evaluate models
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    precision = precision_score(y_test, y_pred, average='weighted')
    print(f"\n{name} Performance:\n{classification_report(y_test, y_pred)}\n Accuracy: {accuracy_score(y_test, y_pred):.4f}\n Precision: {precision:.4f}")
    if precision > best_precision:
        best_precision, best_model, best_model_name = precision, model, name

cv_scores = cross_val_score(
    clone(best_model), X_train, y_train, cv=5, scoring='accuracy')
print(f"\nBest Model: {best_model_name} (Precision: {best_precision:.4f})")

# Save the best model
pipeline = Pipeline([("tfidf", vectorizer), ("model", best_model)])
with open("./Model/best_sentiment_pipeline.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Optimized Sentiment Analysis Model Trained & Saved!")
