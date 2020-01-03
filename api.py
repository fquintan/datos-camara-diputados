import flask
from flask import request, jsonify
from getxml import getAsDict

app = flask.Flask(__name__)
app.config['DEBUG'] = False

@app.route('/', methods=['GET', 'POST'])
def home():
	return 'AAA'

@app.route('/retornarDiputado', methods=['GET', 'POST'])
def diputade():
	if 'prmDiputado' not in request.args:
		return 'Error: debe especificar un valor para prmDiputado'
	return jsonify(getAsDict('diputado', request.args.get('prmDiputado')))


@app.route('/retornarDiputados', methods=['GET', 'POST'])
def diputades():
	return jsonify(getAsDict('diputados_todos', 0))


@app.route('/retornarVotacionesXAnno', methods=['GET', 'POST'])
def votaciones():
	if 'prmAnno' not in request.args:
		return 'Error: debe especificar un valor para prmAnno'
	return jsonify(getAsDict('votaciones_anno', request.args.get('prmAnno')))


@app.route('/retornarVotacionDetalle', methods=['GET', 'POST'])
def votacion():
	if 'prmVotacionId' not in request.args:
		return 'Error: debe especificar un valor para prmVotacionId'
	return jsonify(getAsDict('votacion', request.args.get('prmVotacionId')))


if __name__ == '__main__':
	app.run(port=9090, host='::')