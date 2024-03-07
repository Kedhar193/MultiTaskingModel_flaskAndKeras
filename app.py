#importing necessary libraries 
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_development_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/mlandflask'

db = SQLAlchemy(app)
bcrypt = Bcrypt()
migrate = Migrate(app, db)
login_manager = LoginManager(app)


#loading model that is stored in the project folder with name my_trained_model.h5
model_path = "F:\mlandpy\my_trained_model.h5"
model = load_model(model_path)

#creating user entity with id,username and password fields 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    def is_active(self):
        return True
    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#creating a FlaskForm with username , password , confirm password fields
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
#creating login form for users to login 
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
#signup route and storing user details in the database 
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)
    
#login route and verifying if user is in our database 
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Change 'dashboard' to the route you want to redirect to after login
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')
    return render_template('login.html', form=form)

#logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


#user dashboard available upon successful login 
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)

        
        img = Image.open(file)
        img = img.resize((28, 28))

       

        if img.mode != 'RGB':
            img = img.convert('RGB')

        img_array = np.array(img) / 255.0  # Normalize pixel values
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

       
        predictions = model.predict(img_array)
                
        digit_class = np.argmax(predictions[0])
        color_class = "Green" if predictions[1] > 0.5 else "Red"  # Assuming 0 is red and 1 is green

        

        return render_template('dashboard.html', username=current_user.username, digit_class=digit_class, color_class=color_class)

    return render_template('dashboard.html', username=current_user.username)
if __name__ == '__main__':
    app.run(debug=True)

