from core.facades import banks_facade
from core import app
from flask import jsonify, request


@app.route('/banks', methods=['GET'])
def get_all_banks():
    response_object = {'status': 'success'}
    output = banks_facade.get_all_banks()
    response_object['banks'] = output
    return jsonify(response_object)


@app.route('/banks', methods=['POST'])
def add_new_bank():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    banks_facade.map_and_save_bank(post_data)
    return jsonify(response_object)


@app.route('/banks/<bank_id>', methods=['PUT'])
def update_bank(bank_id):
    response_object = {'status': 'success'}
    banks_facade.update_bank(request.get_json(), bank_id)
    return jsonify(response_object)


@app.route('/banks/<bank_id>', methods=['DELETE'])
def delete_bank(bank_id):
    response_object = {'status': 'success'}
    banks_facade.delete_bank_func(bank_id)
    return jsonify(response_object)
