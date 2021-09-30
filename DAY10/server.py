from flask import Flask
from controllers import book

app = Flask(__name__)
app.register_blueprint(book.app)
app.run(debug=True)