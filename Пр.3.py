from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Декоратор для проверки прав доступа
def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get('role') != role:
                return redirect(url_for('login', next=request.url))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Представление для входа в систему
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Здесь должна быть проверка имени пользователя и пароля
        session['role'] = request.form['role']
        return redirect(url_for('welcome'))
    return render_template('login.html')

# Представление приветствия
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

# Представление для админа
@app.route('/admin')
@role_required('admin')
def admin():
    return 'Админ панель'

# Представление для модератора
@app.route('/moderator')
@role_required('moderator')
def moderator():
    return 'Модератор панель'

# Представление для пользователя
@app.route('/user')
@role_required('user')
def user():
    return 'Пользовательская панель'

if __name__ == '__main__':
    app.run(debug=True)

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Добро пожаловать</title>
</head>
<body>
    {% if session['role'] == 'admin' %}
        <h1>Добро пожаловать, Админ!</h1>
        <!-- Содержимое для админа -->
    {% elif session['role'] == 'moderator' %}
        <h1>Добро пожаловать, Модератор!</h1>
        <!-- Содержимое для модератора -->
    {% else %}
        <h1>Добро пожаловать, Пользователь!</h1>
        <!-- Содержимое для пользователя -->
    {% endif %}
</body>
</html>