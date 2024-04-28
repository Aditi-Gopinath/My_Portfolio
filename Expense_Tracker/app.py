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
    amount = db.Column(db.Float)  
    date = db.Column(db.Date)  
    category = db.Column(db.String(50))
    pay_mode = db.Column(db.String(50))

    def __init__(self, description, amount, date, category, pay_mode):
        self.description = description
        self.amount = amount
        self.date = date
        self.category = category
        self.pay_mode = pay_mode

def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date_str = request.form['date']
        category = request.form['category']
        pay_mode = request.form['pay_mode']

        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            
            new_data = Data(description=description, amount=amount, date=date_obj, category=category, pay_mode=pay_mode)
            db.session.add(new_data)
            db.session.commit()
            flash("Data inserted successfully")
            return redirect(url_for('Index'))


        except Exception as e:
            return f'An error occurred: {str(e)}'
        
@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        expense_id = request.form.get('id')
        my_data = Data.query.get(expense_id)
        if my_data:
            my_data.description = request.form['description']
            my_data.amount = float(request.form['amount'])  # Convert to float
            my_data.date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()  # Convert to date
            my_data.category = request.form['category']
            my_data.pay_mode = request.form['pay_mode']
            
            db.session.commit()
            flash("Expense updated successfully")
        else:
            flash("Expense not found")
        return redirect(url_for('Index'))

@app.route('/delete/<int:id>/',methods = ['GET','POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    flash("Deleted successfully!")
    return redirect(url_for('Index'))


@app.route('/')
def Index():
    all_data = Data.query.all()
    return render_template("index.html", expenses=all_data)

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
