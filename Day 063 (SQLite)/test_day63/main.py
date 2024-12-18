from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column
from sqlalchemy import Integer,String,Float

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///pokemon-colection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True,nullable=False)
    auther: Mapped[str] = mapped_column(String(250),nullable=False)

with app.app_context():
    db.create_all()

# with app.app_context():
#     new_book = Book(id=1,title="Harry Potter",auther="J.K rowling")
#     db.session.add(new_book)
#     db.session.commit()

with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    