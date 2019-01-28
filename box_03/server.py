

try:
    port = 8181
    wsd = WebsocketServer("", port, WebsocketRequestHandler)
    wsd.server_forever()
except KeyboardInterrupt:
    print("shut dwon")
    wsd.socket.close()
