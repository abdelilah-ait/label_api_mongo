# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
# from flask import Response 
# from bson import json_util
import requests
import json

app = Flask(__name__)
#app.config['MONGO_DBNAME'] = 'workspace'
#app.config['MONGO_USERNAME'] = 'admin'
#app.config['MONGO_PASSWORD']  = 'admin'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/workspace'
client = MongoClient("mongodb://127.0.0.1:27017") #host uri
db = client.workspace #Select the database

data=[]
# try:
# 	mongo = PyMongo(app)
# except Exception as error:
#     raise Exception(error)

# db = mongo.db

headers = {
    'Authorization': 'Bearer sandrinecrozat:ef8d27548f4149d61e6923ae5c3030be16f82116',
}

@app.route('/categories', methods=['GET'])
def get_all_categories():
	data = []
	cursor = db.categories.find()
	for categorie in cursor:
		categorie.pop('_id')
		data.append(categorie)
	return jsonify({"response": data})

@app.route('/produits', methods=['GET'])
def get_all_products():
	cursor = db.produits.find().limit(100)
	for produit in cursor:
		produit.pop('_id')
		data.append(produit)
	return jsonify({"response": data})

@app.route('/commandes', methods=['GET'])
def get_all_commandes():
	cursor = db.commandes.find()
	for commande in cursor:
		commande.pop('_id')
		data.append(commande)
	return jsonify({"response": data})

@app.route('/merchants', methods=['GET'])
def get_all_merchants():
	cursor = db.merchants.find()
	for merchant in cursor:
		merchant.pop('_id')
		data.append(merchant)
	return jsonify({"response": data})

@app.route('/paniers', methods=['GET'])
def get_all_cards():
	cursor = db.paniers.find()
	for panier in cursor:
		panier.pop('_id')
		data.append(panier)
	return jsonify({"response": data})



# @app.route('/insert_categories', methods=['GET'])
# def add_categories():
# 	response = requests.get('https://api.sandbox.iceberg.technology/v1/application_category/', headers=headers).text
# 	jdata = json.loads(response)
# 	mongo_categories = db.categories
# 	mongo_categories.insert(jdata)
# 	return redirect(url_for('get_all_categories'))


# @app.route('/insert_produits', methods=['GET'])
# def add_products():
# 	response = requests.get('https://api.sandbox.iceberg.technology/v1/product_channel/1415/viewer/', headers=headers).json()
# 	mongo_produits = db.produits
# 	new_produits = mongo_produits.insert(response)
# 	return redirect(url_for('get_all_products'))

# @app.route('/insert_commandes', methods=['GET'])
# def add_commandes():
# 	response = requests.get('https://api.sandbox.iceberg.technology/v1/merchant_order/', headers=headers).json()
# 	mongo_commandes = db.commandes
# 	new_commandes = mongo_commandes.insert(response)
# 	return redirect(url_for('get_all_commandes'))

# @app.route('/insert_merchants', methods=['GET'])
# def add_merchants():
# 	response = requests.get('https://api.sandbox.iceberg.technology/v1/application/681/merchants/', headers=headers).json()
# 	mongo_merchants = db.merchants
# 	new_merchants = mongo_merchants.insert(response)
# 	return redirect(url_for('get_all_merchants'))

# @app.route('/insert_paniers', methods=['GET'])
# def add_panier():
# 	response = requests.get('https://api.sandbox.iceberg.technology/v1/cart/', headers=headers).json()
# 	mongo_paniers = db.paniers
# 	new_paniers = mongo_paniers.insert(response)
# 	return redirect(url_for('get_all_cards'))

if __name__ == '__main__':
    app.run(debug=True)
