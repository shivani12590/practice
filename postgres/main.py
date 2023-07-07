from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Placeholder data
data = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 3, "name": "Alice"}
]

app = Flask(__name__)

# Configure PostgreSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/person'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


# Define a model for your data
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    # def __init__(self, name):
    #     self.name = name


@app.route('/persons', methods=['POST'])
def create_data():
    new_data = request.get_json()
    name = new_data.get('name', '')
    if name:
        data = Data(name=name)
        db.session.add(data)
        db.session.commit()
        return jsonify({'id': data.id, 'name': data.name}), 201
    else:
        return jsonify({'message': 'Name is required'}), 400


@app.route('/person', methods=['get'])
def get_person():
    return "shivani"


# Read operation (GET request)
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)


# read operation
@app.route('/data/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    for d in data:
        if d['id'] == data_id:
            return jsonify(d)
    return jsonify("data found")


# Create operation (POST request)
@app.route('/data', methods=['POST'])
def create_data1():
    new_data = request.get_json()
    data.append(new_data)
    return jsonify(new_data), 201


# Update operation (PUT request)
@app.route('/data/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    update_data = request.get_json()
    for d in data:
        if d['id'] == data_id:
            d['name'] = update_data['name']
            return jsonify(d)
    return jsonify({'message': 'Data not found'}), 404


# Delete operation (DELETE request)
@app.route('/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    for d in data:
        if d['id'] == data_id:
            data.remove(d)
            return jsonify({'message': 'Data deleted'})
    return jsonify({'message': 'Data not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, port=8080)
