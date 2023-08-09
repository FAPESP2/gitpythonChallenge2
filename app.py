

from flask import Flask, request, jsonify
from models import Store, db  # defined the Store model in models.py
import api_client  # the API client functions in api_client.py
from db import db

app = Flask(__name__)

@app.route('/filters', methods=['GET'])
def get_filters():
    filters = ['Season', 'Cluster', 'Region', 'Region Type', 'Product Model', 'Product Size', 'Product SKU', 'Store Name', 'Store Theme']
    return jsonify(filters)

@app.route('/filters/<string:filter_id>', methods=['POST'])
def get_filter_values(filter_id):
    data = request.get_json()
    if not data or 'filters' not in data:
        return jsonify([])

  
    filter_values = api_client.get_filter_values(filter_id, data['filters'])
    return jsonify(filter_values)

@app.route('/stores', methods=['POST'])
def get_stores():
    data = request.get_json()
    if not data or 'filters' not in data:
        return jsonify([])

    # based on applied filters
    stores = api_client.get_stores(data['filters'])
    return jsonify(stores)

@app.route('/stores/<string:store_name>', methods=['PATCH'])
def update_store(store_name):
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    # store name in the database
    success = api_client.update_store_name(store_name, data['name'])
    if success:
        return '', 200
    else:
        return jsonify({'error': 'Failed to update store name'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
    app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'  
db.init_app(app)

#flask db create # create the db file
