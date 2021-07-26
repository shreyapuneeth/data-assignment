import asyncio
import random
import json

from MockSensorGeneric import MockSensorGeneric


class MockSensor:
    META_DIR = '../meta/'
    VOLTAGE_READINGS = META_DIR + 'voltage.json'
    CURRENT_READINGS = META_DIR + 'current.json'

    def __init__(self, name, min_delay, max_delay):
        self.name = name
        self.sensors = {
            'power': MockSensorGeneric(self.CURRENT_READINGS, self.VOLTAGE_READINGS)
        }
        self.delay = {'min': min_delay, 'max': max_delay}

        self.tasks = []

    async def _publish_reading(self, sensor_name: str, sensor: 'MockSensorGeneric', transport):
        for reading in sensor:
            await transport.publish('sensor.{name}.{type}'.format(name=self.name, type=sensor_name),
                                    reading)
            await asyncio.sleep(random.uniform(self.delay['min'], self.delay['max']))

    def publish_readings(self, transport):
        for sensor_name, sensor in self.sensors.items():
            self.tasks.append(self._publish_reading(sensor_name, sensor, transport))

        return self.tasks


if __name__ == '__main__':
    class PrintTransport:
        async def publish(self, queue_name, data):
            print('{queue}:{data}'.format(queue=queue_name, data=data))


    transport = PrintTransport()
    sensor = MockSensor('test_sensor', 0.01, 0.01)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*sensor.publish_readings(transport)))
