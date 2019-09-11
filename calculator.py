from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/api/add/<data1>/<data2>', methods=['GET'])
def add(data1, data2):
    addition= int(data1) + int(data2)
    data_dict = {}
    data_dict['answer'] = addition
    return jsonify(data_dict)

@app.route('/api/subtract/<data1>/<data2>', methods=['GET'])
def sub(data1, data2):
    addition= int(data1) - int(data2)
    data_dict = {}
    data_dict['answer'] = addition
    return jsonify(data_dict)

@app.route('/api/multiply/<data1>/<data2>', methods=['GET'])
def multi(data1, data2):
    addition= int(data1) * int(data2)
    data_dict = {}
    data_dict['answer'] = addition
    return jsonify(data_dict)

@app.route('/api/divide/<data1>/<data2>', methods=['GET'])
def divide(data1, data2):
    addition= int(data1) / int(data2)
    data_dict = {}
    data_dict['answer'] = addition
    return jsonify(data_dict)


if __name__ == "__main__":
    app.run(debug=True)