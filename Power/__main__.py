from Power import client
import asyncio
from telethon import TelegramClient
from telethon.network.connection import ConnectionTcpAbridged

# ConnectionTcpAbridged is no longer explicitly required in recent versions of telethon

loop = asyncio.get_event_loop()

async def main():
    # Create an instance of the client
    client_instance = client()
    # Start the client
    await client_instance.start()
    # Run the client
    await client_instance.client.run_until_disconnected()
    # connection parameter is not explicitly required
    proxy=None,
    proxy_credentials=None,
    proxy_type=None,
    proxy_secret=None,
    proxy_port=None,
    loop=loop,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
    timeout=None,

if __name__ == "__main__":
    # Create an instance of the client
    client_instance = client()
    # Start the client
    loop.run_until_complete(client_instance.start())
    # Run the client
    loop.run_until_complete(main())
    # Stop the client
    loop.run_until_complete(client_instance.stop())
    loop.close()
    # Add any additional parameters you need for the connection