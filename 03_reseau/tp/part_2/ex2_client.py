import socket

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
tcpsock.connect(("127.0.0.1", 4240))
wfile = tcpsock.makefile("w", encoding="utf-8")

pseudo = input("Entrez un pseudonyme : ")
wfile.write(pseudo + "\n")
wfile.flush()

exit = False
while not exit:
    msg = input("> ")
    wfile.write(msg + '\n')
    wfile.flush()
    if msg == "/quit":
        exit = True

wfile.close()
tcpsock.shutdown(socket.SHUT_RDWR)
tcpsock.close()
