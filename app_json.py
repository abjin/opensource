from flask import Flask, jsonify, request

app = Flask(__name__)

# 1) GET:


@app.route('/api/hello', methods=['GET'])
def api_hello():
    # {"message": "Hello, Flask!"} 형태로 반환
    return jsonify(message='Hello, Flask!')

# 2) POST: 클라이언트가 보낸 JSON 데이터를 받아서 가공 후 응답


@app.route('/api/echo', methods=['POST'])
def api_echo():
    data = request.get_json()                    # 클라이언트가 보낸 JSON 파싱
    name = data.get('name', 'World')             # 필드가 없으면 기본값 'World'
    # 받은 데이터와 인사말을 함께 JSON으로 돌려줌
    # return jsonify(received=data, greeting=f'Hello, {name}!')
    return jsonify(greeting=f'Hello, {name}!')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10005)
