from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.secret_key = "code"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    amount = db.Column(db.Float)  # Corrected type for amount
    date = db.Column(db.Date)  # Changed type to Date

    def __init__(self, description, amount, date):
        self.description = description
        self.amount = amount
        self.date = date

def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date_str = request.form['date']

        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            
            new_user = Data(description=description, amount=amount, date=date_obj)
            db.session.add(new_user)
            db.session.commit()
            flash("Data inserted successfully")
            return redirect(url_for('Index'))


        except Exception as e:
            return f'An error occurred: {str(e)}'
        
@app.route('/update',methods = ['GET','POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        my_data.description = request.form['description']
        my_data.amount = request.form['amount']
        my_data.date = request.form['date']

        db.session.commit()
        flash("expenses added successfully")
        
        return redirect(url_for('Index'))



@app.route('/')
def Index():
    all_data = Data.query.all()
    return render_template("index.html", expenses=all_data)

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
