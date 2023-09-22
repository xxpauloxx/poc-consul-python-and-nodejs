import os
import consul

instance_consul = consul.Consul(host="consul", port="8500")

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    data = instance_consul.kv.get('python-app/data')
    value = data[1].get("Value", b"Default hello world from Python!")
    return f'Consul: {value.decode()}!\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('SERVICE_PORT', 5000)))
