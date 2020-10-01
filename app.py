from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def re_main():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def re_departure(departure):
    return render_template('departure.html')


@app.route('/tours/<id>/')
def re_tours(id):
    return render_template('tour.html')


@app.route('/data/')
def render_all_tours():
    return render_template('all_tours.html')


@app.route('/data/departures/<departure>/')
def render_departure(departure):
    if departure == 'nsk':
        return render_template('departure_nsk.html')


@app.route('/data/tours/<id>/')
def render_tours(id):
    return render_template('tour_id.html')


app.run()
