# explore the flask module and create a web server using flask & python
#flask :- flask is used for creating websites and api and it is a micro web framework.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)
