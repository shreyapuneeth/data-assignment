from nats.aio.client import Client as NATS


class NATSTransport:
    def __init__(self, loop):
        self.nc = NATS()
        self.loop = loop

    async def setup(self):
        await self.nc.connect(loop=self.loop)

    async def publish(self, subject, data):
        await self.nc.publish(subject, str.encode(data))
        await self.nc.flush()

    async def teardown(self):
        await self.nc.close()