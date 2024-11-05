from flask import Flask, render_template, redirect, url_for
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


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


class CafeForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    map_url = StringField(label='Map URL', validators=[DataRequired()])
    img_url = StringField(label='Image URL', validators=[DataRequired()])
    location = StringField(label='Location', validators=[DataRequired()])
    seats = StringField(label='Seats', validators=[DataRequired()])
    has_toilets = SelectField(label='Has Toilets', choices=[('✘'), ('True'), ('False')], validators=[DataRequired()])
    has_wifi = SelectField(label='Has Toilets', choices=[('✘'), ('True'), ('False')], validators=[DataRequired()])
    has_sockets = SelectField(label='Has Toilets', choices=[('✘'), ('True'), ('False')], validators=[DataRequired()])
    can_take_calls = SelectField(label='Has Toilets', choices=[('✘'), ('True'), ('False')], validators=[DataRequired()])
    coffee_price = StringField(label='Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Submit')


def read_all_cafes():
    #reading from the database and adding it to a list
    with app.app_context():
        result = db.session.execute(db.select(Cafe).order_by(Cafe.id))
        all_cafes = []

        for cafe in result.scalars().all():
            cafe_data = {
                'id': cafe.id,
                'name': cafe.name,
                'map_url': cafe.map_url,
                'img_url': cafe.img_url,
                'location': cafe.location,
                'seats': cafe.seats,
                'has_toilets': cafe.has_toilet,
                'has_wifi': cafe.has_wifi,
                'has_sockets': cafe.has_sockets,
                'can_take_calls': cafe.can_take_calls,
                'coffee_price': cafe.coffee_price,
            }



        return all_cafes


all_cafes = read_all_cafes()
# print(all_cafes[0])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cafes')
def cafes():
    cafes = Cafe.query.order_by(Cafe.id).all() #Query the database each time
    return render_template('cafes.html', cafes=cafes)


@app.route('/add', methods=['GET', 'POST'])
def add():
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        #adding it to the database
        # print(cafe_form.name.data)
        new_cafe = Cafe(
            name=cafe_form.name.data,
            map_url=cafe_form.map_url.data,
            img_url=cafe_form.img_url.data,
            location=cafe_form.location.data,
            seats=cafe_form.seats.data,
            has_toilet=(cafe_form.has_toilets.data == 'True'),
            has_wifi=(cafe_form.has_wifi.data == 'True'),
            has_sockets=(cafe_form.has_sockets.data == 'True'),
            can_take_calls=(cafe_form.can_take_calls.data == 'True'),
            coffee_price=cafe_form.coffee_price.data
        )


        with app.app_context():
            db.session.add(new_cafe)
            db.session.commit()
            return redirect(url_for('cafes'))

    return render_template('add.html', form=cafe_form)


#now just figure out how to delete from database

if __name__ == '__main__':
    app.run(debug=True)
