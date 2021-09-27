from flask import Flask
from controllers import book

app = Flask(__name__)
# blueprintをアプリケーションに登録
app.register_blueprint(book.app)
app.run(debug=True)

