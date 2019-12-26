import requests
import xmltodict
import os.path
import json
import time


def parseDiputade(raw):
	if 'Diputado' in raw:
		raw = raw['Diputado']
		del raw['@xmlns:xsi']
		del raw['@xmlns:xsd']
		del raw['@xmlns']
	militancias = raw['Militancias']['Militancia']
	if 'FechaInicio' in militancias: # es una sola
		militancias = [militancias]
	raw['Militancias'] = militancias
	raw['Sexo'] = raw.get('Sexo', {}).get('#text')
	return raw
		
def parseDiputades(raw):
	return [parseDiputade(d) for d in raw['DiputadosColeccion']['Diputado']]
	
def nullParser(raw):
	return raw

def parseVotaciones(raw):
	return [parseVotacion(v) for v in raw['VotacionesColeccion']['Votacion']]

def parseVotacion(raw):
	if 'Votacion' in raw:
		raw = raw['Votacion']
	raw['Quorum'] = raw.get('Quorum', {}).get('#text')
	raw['Resultado'] = raw.get('Resultado', {}).get('#text')
	raw['Tipo'] = raw.get('Tipo', {}).get('#text')
	if 'Votos' in raw:
		raw['Votos'] = [parseDetalleVoto(v) for v in raw['Votos']['Voto']]
	return raw

def parseDetalleVoto(raw):
	raw['OpcionVoto'] = raw.get('OpcionVoto', {}).get('#text')
	return raw

