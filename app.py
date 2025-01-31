import pickle
from flask import Flask, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from db.models import db, User 
from config import Config

# Initialize the Flask app with configurations
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Load sentiment analysis model
with open('./Sentiment_analysis_model/Model/best_sentiment_pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

label_mapping = {0: "Negative", 1: "Neutral", 2: "Positive"}

# Sentiment prediction function

def predict_sentiment(comment):
    prediction = pipeline.predict([comment])[0]
    return label_mapping.get(prediction, "Unknown")


@app.route('/', methods=['GET', 'POST']) 
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))  

    sentiment = None
    if request.method == 'POST':
        comment = request.form['comment']
        sentiment = predict_sentiment(comment)
    return render_template('index.html', sentiment=sentiment)

# Registration route

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = generate_password_hash(password)

        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already exists. Please choose another.", "danger")
            return redirect(url_for('register'))

        new_user = User(username=username, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

# Login route

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash("Login successful!", "success")
            return redirect(url_for('index'))
        else:
            # Store the error message in session
            session['error'] = "Invalid username or password"
            # Redirect to the login page to show SweetAlert
            return redirect(url_for('login'))

    # After handling the form, clear the error message to prevent it from showing again.
    # Remove error message after it's shown
    error_message = session.pop('error', None)
    return render_template('login.html', error_message=error_message)


# Logout route

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)  # Remove username from session
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))


# Delete user

@app.route('/delete_user')
def delete_user():
    if 'user_id' not in session:
        flash("You need to be logged in to delete your account.", "danger")
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if user:
        db.session.delete(user)
        db.session.commit()
        session.pop('user_id', None)
        flash("Your account has been deleted.", "info")

    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # host = '0.0.0.0' allows the app to be accesisble from any device on the network
    app.run(debug=True, port=app.config['PORT'])
