import json
import flask
import requests
from flask import jsonify
from configparser import ConfigParser
from Data.Json import Json
from Data.JsonToExcel import JsonToCsvExcel

app = flask.Flask(__name__)
config = ConfigParser()
config.read('API.properties')

API_KEY = config.get('DEFAULT', 'API_KEY')
FILE_TYPE = config.get('DEFAULT', 'FILE_TYPE')
FILE_NAME = config.get('DEFAULT', 'FILE_NAME')
URL = "https://www.virustotal.com/api/v3/files/"

@app.route('/')
def homepage():
	return 'VirusTotal API: Keep searching!'

@app.route('/hash_search', methods=['GET'])
def hash_search_info():
    return 'Use the following syntax to search on API hashsearch/valid_hash'

@app.route('/hash_search/<string:query>')
def hash_search(query):
    hash_url = URL + query
    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }
    response = requests.get(hash_url, headers=headers)

    if response.status_code == 200:
        attributes = response.json()
        json_processor = Json(attributes)
        relevant_data = json_processor.extract_relevant_content()
        dump_json = json.dumps(relevant_data)
        conversor = JsonToCsvExcel(json.loads(dump_json))
        if(FILE_TYPE == 'EXCEL'):
            conversor.export_table_excel(FILE_NAME)
        elif(FILE_TYPE == 'CSV'):
            conversor.export_table_csv(FILE_NAME)
        else:
            print('Arquivo não especificado ou não reconhecido. Informações serão apenas transmitidas no navegador')


        return jsonify(relevant_data)
        #return json_processor.json_data
    else:
        return jsonify({"Erro": "Hash não encontrado"}), response.status_code

if __name__ == '__main__':
    #response = requests.post(url, data=payload, headers=headers)
    app.run(host='0.0.0.0')

