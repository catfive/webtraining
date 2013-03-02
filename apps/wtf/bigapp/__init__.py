from flask import Flask

app = Flask(__name__)
app.debug=True
app.secret_key="It's a secret to no one"
import urls