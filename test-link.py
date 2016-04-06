from flask import Flask
from redis import Redis
import netifaces as ni
import logging
import sys
import os
import platform

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
app = Flask(__name__)
redis = Redis(host='redis', port=6379)


def add_record():
    ni.ifaddresses('eth0')
    ip = ni.ifaddresses('eth0')[2][0]['addr']
    logging.info('container eth0 ip address {}'.format(ip))
    redis.set(ip, ip)


def ping(host):
    """
    Returns True if host responds to a ping request
    """

    # Ping parameters as function of OS
    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + host) == 0


@app.route('/')
def get_network_status():
    ips = redis.keys()
    message = []
    ni.ifaddresses('eth0')
    ip = ni.ifaddresses('eth0')[2][0]['addr']
    message.append('current ip is {}'.format(ip))
    for ip in ips:
        res = ping(ip)
        str_message = 'ping {} response is {}'.format(ip, res)
        logging.info(str_message)
        message.append(str_message)
    return '<br/>'.join(message)

if __name__ == '__main__':
    add_record()
    app.run(host='0.0.0.0', debug=True)
