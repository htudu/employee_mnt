from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<p>Hello, Shital & Hambira!</p>
                Welcome to the CI/CD !
            """


if __name__ == "__main__":
    app.run()