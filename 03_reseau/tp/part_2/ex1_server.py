import asyncio

@asyncio.coroutine
def _handle_client(client_reader, client_writer):
    nickname = yield from client_reader.readline()
    nickname = nickname.decode('utf-8').strip()
    print('*** {} a rejoint la discussion'.format(nickname))

    while True:
        msg = yield from client_reader.readline()
        msg = msg.decode('utf-8')
        if not msg or msg[:5] == '/quit':
            break
        print('<{}> {}'.format(nickname, msg.strip()))

    print('*** {} a quitté la discussion'.format(nickname))

def main(port=4240):
    loop = asyncio.get_event_loop()
    coro = asyncio.streams.start_server(_handle_client, '', port, loop=loop)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == '__main__':
    main()
