# bookmanager.py
import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file

db = SQLAlchemy(app)


class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title>: {}".format(self.title)


@app.route("/", methods=['GET', 'POST'])
def home():
    added = False
    if request.form:
        title = request.form.get('title')
        book = Book(title=title)
        db.session.add(book)
        db.session.commit()
        added = True

    books = Book.query.all()
    return render_template('home.html', books=books, added=added)


@app.route("/update", methods=['POST'])
def update():
    new_title = request.form.get('new-title')
    old_title = request.form.get('old-title')

    book = Book.query.filter_by(title=old_title).first()
    book.title = new_title
    db.session.commit()
    return redirect('/')


@app.route("/delete", methods=['POST'])
def delete():
    title = request.form.get('title')
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
