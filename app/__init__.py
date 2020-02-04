from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('xdevbot.cfg', silent=True)
print(app.config['SECRET_KEY'])

from app import routes  # noqa: E402 F401
