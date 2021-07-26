from MockSensor import MockSensor
from NATSTransport import NATSTransport
import asyncio


def main(loop):
    transport = NATSTransport(loop)
    loop.run_until_complete(transport.setup())
    sensor = MockSensor('test_sensor', 0.01, 0.01)
    loop.run_until_complete(asyncio.gather(*sensor.publish_readings(transport)))
    loop.run_until_complete(transport.teardown())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    main(loop)
    sensor = MockSensor('test_sensor', 0.01, 0.01)

    print('done')
