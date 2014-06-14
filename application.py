import flask
from flask import jsonify
app = flask.Flask(__name__)

#Set application.debug=true to enable tracebacks on Beanstalk log output. 
#Make sure to remove this line before deploying to production.
app.debug=True

@app.route('/index')
@app.route('/')
def index():
    return "nothing to see here"


@app.route('/api/v1.0/timeseries/<timeAggregate>/<localeAggregate>/cumulative/', methods=['GET'])
def get_timeseries_cumulative():
    return jsonify({'bert': 'bert'})

@app.route('/api/v1.0/timeseries/<timeAggregate>/<localeAggregate>/', methods=['GET'])
def get_timeseries(timeAggregate, localeAggregate):
    return jsonify({'bert': timeAggregate, "bert2": localeAggregate})

@app.route('/api/v1.0/timeseries/<timeAggregate>/<localeAggregate>/<locale>/cumulative/', methods=['GET'])
def get_single_timeseries():
    return jsonify({'bert': 'bert'})

@app.route('/api/v1.0/timeseries/<timeAggregate>/<localeAggregate>/<locale>/', methods=['GET'])
def get_single_timeseries_cumulative():
    return jsonify({'bert': 'bert'})




if __name__ == '__main__':
    app.run(debug=True)