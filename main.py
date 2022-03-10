import sqlite3
from flask import Flask, render_template, url_for, redirect, request, jsonify
from scripts.routeBuilder import make_route
from scripts.base_manager import get_arrow
app = Flask(__name__)

res = []
nextTarget = 0

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_route')
def getRandomRoute():
    connection = sqlite3.connect('db.sqlite')

    cur = connection.cursor()
    return jsonify(list(cur.execute("select max(marker_id) from routes")))


@app.route('/get_target', methods=['GET', 'POST'])
def getTarget():
    return 200


@app.route('/custom_route', methods=['GET', 'POST'])
def customRoute():
    print("here we go")
    routes = list(map(int, request.get_json(force=True)[0].split()))
    print(routes)
    global res
    res = []

    for i in range(len(routes) - 1):
        try:
            res.pop()
        except:
            pass
        res += make_route(routes[i], routes[i + 1])

    print(res)
    global nextTarget
    nextTarget = 0
    return 'Sucesss', 200


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('gallery.html')


@app.route('/navigation_lobby', methods=['GET', 'POST'])
def navigation_lobby():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('navigationLobby.html')


@app.route('/navigation', methods=['GET', 'POST'])
def navigation():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('navigation.html')


@app.route('/create_route', methods=['GET', 'POST'])
def create_route():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('createRoute.html')

@app.route('/panorama1', methods=['GET', 'POST'])
def panorama1():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('panorama1.html')

@app.route('/panorama2', methods=['GET', 'POST'])
def panorama2():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('panorama2.html')

@app.route('/photobooth', methods=['GET', 'POST'])
def photobooth():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('photobooth.html')

@app.route('/portal', methods=['GET', 'POST'])
def portal():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('portal.html')


@app.route('/game', methods=['GET', 'POST'])
def toGame():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('game.html')


@app.route('/get_current_id', methods=['GET', 'POST'])
def getCurrentId():
    global nextTarget
    nextTarget += 1
    print("nT")
    print(res[nextTarget - 1])
    return str(res[nextTarget - 1])


@app.route('/get_current_arrow', methods=['GET', 'POST'])
def getCurrentArrow():
    if nextTarget == len(res) - 1:
        return "0"
    else:
        arrowDir = get_arrow(res[nextTarget - 1], res[nextTarget])
        print("{} {}".format(res[nextTarget], res[nextTarget + 1]))
        print("aD")
        print(arrowDir)
        return str(arrowDir)


if __name__ == '__main__':
    app.run()
