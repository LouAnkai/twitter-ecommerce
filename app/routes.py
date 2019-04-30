from app import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/index')
def index():
    products = [
            {
                'id': 1001,
                'title': 'Soap',
                'price': 3.98,
                'desc': 'Very clean soapy soap, descriptive text'
            },
            {
                'id': 1002,
                'title': 'Grapes',
                'price': 4.56,
                'desc': 'A bundle of grapey grapes, yummy'
            },
            {
                'id': 1003,
                'title': 'Pickles',
                'price': 5.67,
                'desc': 'A jar of pickles is pickly'
            },
            {
                'id': 1004,
                'title': 'Juice',
                'price': 2.68,
                'desc': 'Yummy orange juice'
            }
        ]
    return render_template('index.html', title='Home', products=products)
