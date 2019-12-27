import requests
import xmltodict
import os.path
import os
import json
import parsers


tiposConsulta = {
	'diputado': {
		'url': 'http://opendata.camara.cl/camaradiputados/WServices/WSDiputado.asmx/retornarDiputado',
		'param': 'prmDiputadoId',
		'parser': parsers.parseDiputade
	},
	'diputados_todos': {
		'url': 'http://opendata.camara.cl/camaradiputados/WServices/WSDiputado.asmx/retornarDiputados',
		'parser': parsers.parseDiputades
	},
	'votaciones_anno': {
		'url': 'http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarVotacionesXAnno',
		'param': 'prmAnno',
		'parser': parsers.parseVotaciones,
	},
	'votacion': {
		'url': 'http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarVotacionDetalle',
		'param': 'prmVotacionId',
		'parser': parsers.parseVotacion,
	}
}

def getCachePath(tipo, value):
	if tipo not in tiposConsulta:
		return None
	cache_dir = os.getenv('CACHE_PATH', 'cache')
	path = cache_dir + '/' + tipo
	if not os.path.exists(path):
	    os.makedirs(path)
	path = path + '/%s' % value
	return path

def getAsDict(tipo, value, ignoreCache=False):
	if tipo not in tiposConsulta:
		return ''
	path = getCachePath(tipo, value)
	r = getXml(tipo, value, ignoreCache)
	asRawDict = xmltodict.parse(r)
	asJson = tiposConsulta[tipo].get('parser', parsers.nullParser)(asRawDict)

	# with open(path+'.json', 'w') as f:
	# 	json.dump(asJson, f, indent=2, ensure_ascii=False)

	return asJson


def getXml(tipo, value, ignoreCache=False):
	if tipo not in tiposConsulta:
		return ''
	path = getCachePath(tipo, value)
	URL = tiposConsulta[tipo]['url']
	params = {}
	if 'param' in tiposConsulta[tipo]:
		params[tiposConsulta[tipo]['param']] = value
	if ignoreCache or not os.path.exists(path+'.xml'):		
		r = requests.get(url=URL, params=params)
		if r.status_code != 200:
			print('Error status_code %s para %s, params: %s' % (r.status_code, URL, params))
			return ''
		with open(path+'.xml', 'w') as f:
			f.write(r.text)
		return r.text
	
	with open(path+'.xml', 'r') as f:
		r = f.read()
		return r


if __name__ == '__main__':
    print(json.dumps(getAsDict('diputado', 803), indent=2, ensure_ascii=False))