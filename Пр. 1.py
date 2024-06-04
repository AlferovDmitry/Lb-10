from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.now().time()
    if current_time >= datetime.strptime('06:00', '%H:%M').time() and current_time < datetime.strptime('12:00', '%H:%M').time():
        greeting = "Доброе утро"
    elif current_time >= datetime.strptime('12:00', '%H:%M').time() and current_time < datetime.strptime('18:00', '%H:%M').time():
        greeting = "Добрый день"
    elif current_time >= datetime.strptime('18:00', '%H:%M').time() and current_time < datetime.strptime('00:00', '%H:%M').time():
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
В шаблоне index.html вы можете использовать Jinja2 синтаксис для отображения приветствия:

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Приветствие</title>
</head>
<body>
    <h1>{{ greeting }}</h1>
</body>
</html>