import sqlite3
from flask import Flask, render_template, url_for, redirect, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_route')
def getRandomRoute():
    connection = sqlite3.connect('db.sqlite')

    cur = connection.cursor()
    return jsonify(list(cur.execute("select max(marker_id) from routes")))


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('gallery.html')

@app.route('/navigation', methods=['GET', 'POST'])
def navigation():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('navigation.html')

@app.route('/panorama1', methods=['GET', 'POST'])
def panorama1():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('panorama1.html')

@app.route('/panorama2', methods=['GET', 'POST'])
def panorama2():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('panorama2.html')

@app.route('/photobooth', methods=['GET', 'POST'])
def photobooth():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('photobooth.html')

@app.route('/portal', methods=['GET', 'POST'])
def portal():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('portal.html')


if __name__ == '__main__':
    app.run()
