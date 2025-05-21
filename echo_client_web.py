import socket

HOST = '220.149.232.226'
PORT = 10005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # 요청 문자열 구성
    request = (
        "GET / HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    s.sendall(request.encode('utf-8'))

    # 응답 읽기
    response = b''
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk

    print(response.decode('utf-8'))
