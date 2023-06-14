from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
