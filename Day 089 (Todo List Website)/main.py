from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class TodoList(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)


with app.app_context():
    db.create_all()


#not adding to the db something wrong, when i press button it should add to db

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    task_text = request.form['task']
    if task_text:
        new_task = TodoList(task=task_text)
        with app.app_context():
            db.session.add(new_task)
            db.session.commit()
    return redirect(url_for('home'))

@app.route('/delet_all', methods=['GET', 'POST'])
def delete_all():
    with app.app_context():
        db.session.query(TodoList).delete()
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/', methods=['GET', 'POST'])
def home():
    with app.app_context():
        result = db.session.execute(db.select(TodoList).order_by(TodoList.task))
        all_tasks = result.scalars().all()
        num = 0
        for task in all_tasks:
            num += 1
        print(num)
    return render_template('home.html', all_tasks=all_tasks, number_of_tasks=num)





if __name__ == '__main__':
    app.run(debug=True)

#Todo: add a delete button to delete all in database
