import sys, socket, re, time
from PyQt5.QtGui import QColor
import Record

HOST = '127.0.0.1'
PORT = 23

group_to_display = [0]

class TelnetServer():
    def __init__(self, sig):
        self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv_sock.bind((HOST, PORT))
        self.serv_sock.listen(10)
        self.sig = sig

    def run_forever(self):

        while True:
            client_sock, client_addr = self.serv_sock.accept()
            cummulation = ''
            print('Connected by', client_addr)

            while True:
                data = client_sock.recv(1024)
                # ignore telnet negotiation
                try:
                    cummulation = cummulation + data.decode("utf-8")
                except Exception:
                    pass

                result = Record.Record.parse(cummulation)

                if result:
                    print(result.to_text())
                    if result.group in group_to_display:
                        self.sig.emit(result.to_text(), QColor(0, 0, 255))  # display result

                    # self.sig.emit(
                    #     '{} - thread 2 variant 1.\n'.format(str(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))),
                    #     QColor(0, 0, 255)
                    # )
                    cummulation = ''

                if not data:
                    break
                # client_sock.sendall(data)

            client_sock.close()


