# **NL Pulse AI ฉᲩ 🎓**

## **Project Description**

This project is a web-based sentiment analysis application built with Flask, a lightweight Python web framework. The app allows users to input text (such as a comment), and it then predicts the sentiment of the text (whether it is **Negative**, **Neutral**, or **Positive**). The sentiment prediction is powered by a machine learning model trained on text data and stored as a pickle file (`best_sentiment_pipeline.pkl`).

The application also includes user authentication and management features, such as **user registration**, **login**, **logout**, and **account deletion**. The app uses a simple relational database (via SQLAlchemy) to store user data securely with password hashing.

## **Technologies Used**
- **Flask**: Python web framework used to build the application and handle routing.
- **SQLAlchemy**: ORM used to interact with the database.
- **Pickle**: Used to load the pre-trained sentiment analysis model.
- **Werkzeug**: Provides utilities for password hashing and checking.
- **Scikit-learn**: For machine learning tasks like sentiment prediction (used for loading the model and making predictions).
- **Bootstrap**: For simple and responsive frontend styling (via HTML/CSS).
- **SweetAlert2**: Used to show alerts and notifications in the frontend.
- **SQLite**: Simple SQL database for storing user information.
- **Langdetect**: For language detection in the text (optional for further improvements).
- **NLTK**: For text preprocessing and tokenization.

## **Features**
1. **User Registration**: Users can create an account with a unique username and password.
2. **Login System**: Users can log in with their username and password.
3. **Sentiment Prediction**: After logging in, users can submit comments, and the app will predict whether the sentiment of the comment is **Positive**, **Neutral**, or **Negative**.
4. **SweetAlert Notifications**: Alerts are displayed for errors (invalid credentials), successful login, or registration.
5. **Account Management**: Users can log out or delete their account.
6. **Responsive Frontend**: The app has a simple, responsive interface designed with HTML, CSS, and SweetAlert2 for notifications.

## **Installation and Setup**

### **Step 1: Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/skmirajulislam/NLPulse-AI.git
cd NLPulse-AI
```

### **Step 2: Set up Virtual Environment**

Create and activate a virtual environment for Python:

```bash
# Install virtualenv if not installed
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### **Step 3: Install Dependencies**

Install the required Python libraries listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### **Step 4: Configure the App**

In the `config.py` file, you can configure settings such as the database URI, secret key, and other configurations for Flask. Here's an example configuration:

```python
class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = 5000
```

### **Step 5: Initialize the Database**

Ensure that your database schema is set up before running the application. You can do this by running the following command:

```bash
python app.py
```

This will automatically create the necessary database tables (if they don't exist already) when you start the app.

### **Step 6: Run the Flask App**

Now, you can start the Flask app:

```bash
python app.py
```

By default, the app will run at `http://127.0.0.1:8000/`. You can access it in your web browser.

### **Step 7: Access the Application**

- Open the browser and visit `http://127.0.0.1:8000/`.
- You will be prompted to log in or register if you haven't created an account already.

## **Using the Application**

1. **Registration**: When you visit the home page, you can create a new account by filling out the registration form with a username and password.
2. **Login**: After successful registration, you can log in using the username and password you created.
3. **Sentiment Analysis**: Once logged in, you can submit comments for sentiment analysis. The app will show whether the comment is **Positive**, **Neutral**, or **Negative**.
4. **Logout**: You can log out at any time, which will clear the session.
5. **Delete Account**: If you wish to delete your account, you can do so from the settings or profile page, and your data will be removed from the database.

## **Project Setup and Workflow**

1. **User Authentication Flow**:
   - The app uses Flask's `session` to store the user's login status.
   - Users are redirected to the login page if they are not authenticated.
   - Passwords are hashed using Werkzeug's `generate_password_hash` function to ensure security.
  
2. **Sentiment Prediction Flow**:
   - When a user submits a comment, the sentiment model (`best_sentiment_pipeline.pkl`) predicts the sentiment of the comment.
   - The `predict_sentiment` function makes use of the pre-trained machine learning model to generate predictions and map them to labels such as "Negative", "Neutral", and "Positive".

## **Potential Improvements**
- **Multi-language support**: Add support for multiple languages using a language detection library (like `langdetect`).
- **Machine learning model update**: Allow the user to upload new training data and retrain the sentiment model.
- **User profile**: Implement additional user profile features like updating passwords, email, or profile pictures.
- **Deployment**: Deploy the application to a cloud service like Heroku or AWS for production use.

## **Requirements**
- Python 3.x
- Flask
- Flask-SQLAlchemy
- scikit-learn
- imbalanced-learn
- nltk
- langdetect
- werkzeug

## **To Run the Application Locally:**
1. Clone the repository.
2. Set up a Python virtual environment.
3. Install the required dependencies from `requirements.txt`.
4. Run `app.py` to start the local development server.
5. Open your browser and visit `http://127.0.0.1:8000/` to interact with the app.

## **Example Screenshots**

### **Login Page**
![Login Page](https://github.com/skmirajulislam/NLPulse-AI/blob/master/images/NLpulse4.png)

### **Register Page**
![Register Page](https://github.com/skmirajulislam/NLPulse-AI/blob/master/images/NLpulse5.png)

### **Sentiment Analysis Result**
![Sentiment Analysis](https://github.com/skmirajulislam/NLPulse-AI/blob/master/images/NLpulse2.png)

### **Logout Page**
![Logout Page](https://github.com/skmirajulislam/NLPulse-AI/blob/master/images/NLpulse3.png)

### **Delete Account Page**
![Delete Account Page](https://github.com/skmirajulislam/NLPulse-AI/blob/master/images/NLpulse1.png)

## **Contributing**
Contributions are welcome! Feel free to fork the project and create a pull request. If you find any issues or have suggestions for improvement, open an issue on GitHub.
