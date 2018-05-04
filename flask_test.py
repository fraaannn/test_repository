from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h2>welcome to cookie pool system</h2>'


@app.route('/<website>/random')
def random(website):
    data = '<h2>%s</h2>'%str(website)
    return data


if __name__ == "__main__":
    app.run()