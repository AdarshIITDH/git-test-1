from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    return str(data['a'] + data['b'])

if __name__ == '__main__':
    app.run()

# curl -X POST -H "Content-Type: application/json" \
#     -d '{"a": 3, "b": 5}' \
#     http://127.0.0.1:5000/add
