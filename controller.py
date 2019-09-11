from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def visit_root():
    return render_template('sample.html')

@app.route('/example', methods=['GET'])
def new_route():
    return "This is a new route!"

@app.route('/return_data/<data>', methods=['GET'])
def return_data(data):
    # your python logic here
    return "<h1> {} </h1>".format(data)

if __name__ == "__main__":
    app.run(debug=True)

