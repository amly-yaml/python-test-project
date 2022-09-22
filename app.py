from crypt import methods
from flask import Flask , redirect , render_template, request
from flask_login import LoginManager , UserMixin , login_required ,login_user, logout_user
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///register.db"
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='797979'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class Register(UserMixin, db.Model):
    id = db.Column(db.Integer, nullable = False, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(20), nullable = False)

    def __repr__(self) -> str:
        return f"Register('{self.username}','{self.email}')"


class Expense(db.Model):
    id = db.Column(db.Integer, nullable = False, primary_key = True)
    expensename = db.Column(db.String(100), nullable = False)
    amount = db.Column(db.Integer, nullable = False)
    category = db.Column(db.String(50), nullable = False)


@login_manager.user_loader
def get(id):
    return Register.query.get(id)

@app.route('/',methods=['GET'])
@login_required
def get_home():
    return render_template('login.html')

@app.route('/login',methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/signup',methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/login',methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = Register.query.filter_by(email=email).first()
    login_user(user)
    return redirect('/user')

@app.route('/signup',methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    user = Register(username=username,email=email,password=password)
    db.session.add(user)
    db.session.commit()
    user = Register.query.filter_by(email=email).first()
    login_user(user)
    return redirect('/user')

@app.route('/logout',methods=['GET'])
def logout():
    logout_user()
    return redirect('/login')

@app.route('/user', methods=['GET'])
def user():
    getAllexpenses = Expense.query.all()
    total = 0
    t_food_amount = 0
    t_entertainment_amount = 0
    t_other_amount = 0
    t_business_amount = 0 
    for expense in getAllexpenses:
        total += expense.amount
        if expense.category == 'food':
            t_food_amount += expense.amount
        elif expense.category == 'business':
            t_business_amount += expense.amount
        elif expense.category == 'entertainment':
            t_entertainment_amount += expense.amount
        elif expense.category == 'other':
                t_other_amount += expense.amount

    return render_template('user.html', expense=getAllexpenses, expenses = getAllexpenses, t_food=t_food_amount, t_business=t_business_amount, 
    t_entertainment=t_entertainment_amount, t_other=t_other_amount, t_total=total) 



if __name__ == '__main__':
    app.run(debug=True)
