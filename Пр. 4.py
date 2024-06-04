from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///supermarket.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        new_product = Product(name=name, quantity=quantity)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Список товаров</title>
</head>
<body>
    <h1>Список товаров</h1>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - Количество: {{ product.quantity }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add_product') }}">Добавить товар</a>
</body>
</html>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Добавление товара</title>
</head>
<body>
    <h1>Добавление товара</h1>
    <form method="post">
        Название: <input type="text" name="name" required>
        Количество: <input type="number" name="quantity" required>
        <input type="submit" value="Добавить">
    </form>
</body>
</html>