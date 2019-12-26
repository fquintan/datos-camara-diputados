import flask
from flask import request, jsonify
from getxml import getAsDict

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def home():
	return 'AAA'

@app.route('/retornarDiputado', methods=['GET', 'POST'])
def diputade():
	if 'prmDiputado' not in request.args:
		return 'Error: debe especificar un valor para prmDiputado'
	
	return jsonify(getAsDict('diputado', request.args.get('prmDiputado')))

app.run(port=9090, host='::')