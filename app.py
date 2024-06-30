from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    #connect to cozy app
    # make call to fetch story
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)