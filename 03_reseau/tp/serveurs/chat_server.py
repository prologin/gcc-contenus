import asyncio
import time

messages = []
new_message = asyncio.Condition()

# Rate limit = `RATE_MESSAGE` / `RATE_SECONDS`
RATE_MESSAGE = 100
RATE_SECONDS = 1


async def _send_all(msg):
    print(msg)
    async with new_message:
        messages.append(msg + '\n')
        new_message.notify_all()


async def _handle_rclient(client_reader, client_writer):
    nickname = await client_reader.readline()
    nickname = nickname.decode('utf-8').strip()
    await _send_all('*** {} a rejoint la discussion'.format(nickname))
    messages = 0
    last_time = time.time()

    while True:
        msg = await client_reader.readline()
        msg = msg.decode('utf-8')

        if messages == RATE_MESSAGE:
            current_time = time.time()
            if (current_time - last_time) < RATE_SECONDS:
                await asyncio.sleep(RATE_SECONDS - (current_time - last_time))
            messages = 0
            last_time = current_time
        messages += 1

        # empty message, discarding
        if (len(msg.strip()) == 0):
            continue
        if not msg or msg[:5] == '/quit':
            break
        await _send_all('<{}> {}'.format(nickname, msg))

    await _send_all('*** {} a quitté la discussion'.format(nickname))


async def _handle_wclient(client_reader, client_writer):
    i = len(messages)
    while True:
        async with new_message:
            await new_message.wait()
            for msg in messages[i:len(messages)]:
                client_writer.write(bytes(msg, encoding='utf-8'))
            i = len(messages)


def main(rport=4242, wport=4241):
    loop = asyncio.get_event_loop()
    rcoro = asyncio.streams.start_server(_handle_rclient, '', rport, loop=loop)
    wcoro = asyncio.streams.start_server(_handle_wclient, '', wport, loop=loop)
    rserver = loop.run_until_complete(rcoro)
    wserver = loop.run_until_complete(wcoro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    rserver.close()
    wserver.close()
    loop.run_until_complete(rserver.wait_closed())
    loop.run_until_complete(wserver.wait_closed())
    loop.close()


if __name__ == '__main__':
    main()
