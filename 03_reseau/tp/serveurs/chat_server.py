import asyncio
import time

messages = []
new_message = asyncio.Condition()
spammers = []

# Rate limit = `RATE_MESSAGE` / `RATE_SECONDS`
RATE_MESSAGE = 10
RATE_SECONDS = 1


async def _send_all(msg):
    print(msg)
    async with new_message:
        messages.append(msg)
        new_message.notify_all()


async def _handle_rclient(client_reader, client_writer):
    # Get peername to send spam warning
    socket = client_writer.get_extra_info('socket')
    peername = None
    if socket is not None:
        peername = socket.getpeername()[0]

    # Get nickname
    nickname = await client_reader.readline()
    nickname = nickname.decode('utf-8').strip()
    await _send_all(f'*** {nickname} a rejoint la discussion ({peername})')
    messages = 0
    last_time = time.time()

    while True:
        msg = await client_reader.readline()
        msg = msg.decode('utf-8')

        # empty message, discarding
        if (len(msg.strip()) == 0):
            continue

        # spam detection routine
        if messages == RATE_MESSAGE:
            current_time = time.time()
            if (current_time - last_time) < RATE_SECONDS:
                spammers.append((peername, nickname))
                print(f'{nickname} ({peername}) is spamming.')
                async with new_message:
                    new_message.notify_all()
                await asyncio.sleep(RATE_SECONDS - (current_time - last_time))
                spammers.remove((peername, nickname))
            messages = 0
            last_time = current_time
        messages += 1

        if not msg or msg[:5] == '/quit':
            break
        await _send_all(f'<{nickname}> {msg}')

    await _send_all(f'*** {nickname} a quitté la discussion')


async def _handle_wclient(client_reader, client_writer):
    i = len(messages)
    socket = client_writer.get_extra_info('socket')
    peername = None
    if socket is not None:
        peername = socket.getpeername()[0]

    while True:
        async with new_message:
            await new_message.wait()

            if any(peername in spammer for spammer in spammers):
                client_writer.write(bytes(
                    "Spam détecté ! (Plus de 10 messages par secondes)\n",
                    encoding='utf-8'))

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
