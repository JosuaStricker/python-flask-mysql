from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Germany',
    'salary': 'Rs.  15,00,000'
}, {
    'id': 2,
    'title': 'Dev Python Backend',
    'location': 'France',
}, {
    'id': 3,
    'title': 'Dev Flask Frontend',
    'location': 'Swiss',
    'salary': 'EUR 987000'
}]


@app.route("/")
def helloworld():
    return render_template('home.html',
                           jobs=JOBS,
                           company_name='Chrono Enigma')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
