import json
from collections import defaultdict


class MockSensorGeneric:

    def calcPower(self, curr: list, volt: list):
        curr_list = [{
            'time': d['time'],
            'value': d['value']
        } for d in curr]

        curr_list = curr_list[0:10000]

        volt_list = [{
            'time': d['time'],
            'value': d['value']
        } for d in volt]

        volt_list = volt_list[0:10000]

        power_dic = []
        for x in curr_list:
            for y in volt_list:
                if x['time'] == y['time']:
                    power_dic.append({'time': x['time'], 'value': round(x['value'] * y['value'], 2)})

        return power_dic

    def __init__(self, source_file1: str, source_file2: str):
        with open(source_file1) as file:
            self.measurements_curr = iter(json.load(file))

        with open(source_file2) as file:
            self.measurements_volt = iter(json.load(file))

        self.p = iter(self.calcPower(self.measurements_curr, self.measurements_volt))

    def __iter__(self):
        return self

    def __next__(self):
        return json.dumps(next(self.p))


if __name__ == '__main__':
    sensor = MockSensorGeneric('../meta/voltage.json', '../meta/current.json')

    power_dic = MockSensorGeneric.calcPower(sensor.measurements_curr, sensor.measurements_volt)
    # printing
    print(power_dic)
