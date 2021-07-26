import json

a = [4,5]
with open('test.txt', 'w') as f:
    f.write(json.dumps(a))
