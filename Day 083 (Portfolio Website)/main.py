from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "1234"
Bootstrap5(app)


class ContactForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email_address = StringField(label='Email Address', validators=[DataRequired()])
    message = TextAreaField(label='Message', validators=[DataRequired()])
    subject = StringField(label='Subject', validators=[DataRequired()])
    submit = SubmitField(label="Send")


@app.route('/', methods=["GET", "POST"])
def homepage():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        print(contact_form.name.data)
    return render_template("index.html", form=contact_form)


if __name__ == "__main__":
    app.run(debug=True)
