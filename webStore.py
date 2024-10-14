from flask import Flask, render_template, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc, desc
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), index=True, unique=True)
    artist = db.Column(db.String(64))
    price = db.Column(db.Integer)  
    description = db.Column(db.Text)
    image = db.Column(db.String(32))
    environment = db.Column(db.Integer);

    
@app.route('/', methods=['GET', 'POST'])
def Gallery():
    albums = Album.query.all()

    if 'basket' not in session:
        session['basket'] = {}
    
    basket = session['basket']

    sort_by = request.args.get('sort_by')
    if sort_by == 'name':
        albums = Album.query.order_by(asc(Album.name)).all()
    elif sort_by == 'price':
        albums = Album.query.order_by(asc(Album.price)).all()
    elif sort_by == 'environment':
        albums = Album.query.order_by(asc(Album.environment)).all()

    if request.method == 'POST':
        quantity = request.form['quantity']
        album_id = request.form['item_id']
        basket[album_id] = quantity
        session['basket'] = basket
        session.modified = True
        print(session['basket'])
        return redirect(url_for('Basket'))
    
    return render_template('Gallery.html', albums=albums)

@app.route('/Album/<int:itemId>', methods=['GET', 'POST'])
def SingleProduct(itemId):
    album = Album.query.get(itemId)

    if 'basket' not in session:
        session['basket'] = {}
    
    basket = session['basket']

    if request.method == 'POST':
        quantity = request.form['quantity']
        album_id = request.form['item_id']
        basket[album_id] = quantity
        session['basket'] = basket
        session.modified = True
        print(session['basket'])
        return redirect(url_for('Basket'))

    return render_template('SingleProduct.html', album=album)


@app.route('/Basket', methods=['GET', 'POST'])
def Basket():
    basket = session.get('basket', {})
    albums = {}
    if request.method == 'POST':
        id = request.form['remove_id']
        del basket[id]
        session['basket'] = basket
        session.modified = True
        return redirect(url_for('Basket'))

    total = 0
    for item in basket:
        album = Album.query.filter_by(id=item).first()
        albums[item] = {'name': album.name, 'price': album.price, 'image': album.image, 'artist': album.artist}
        total += (int(basket[item]) * albums[item]['price'])

    print(albums)
    return render_template('Basket.html', basket=basket, albums=albums, total=round(total, 2))

    



@app.route('/Checkout')
def Checkout():
    return render_template('Checkout.html')



if __name__ == '__main__':
    app.run(debug=True, port=5050)


