import network
from env import dotenv

env = dotenv('.env')
env.scan()

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

sta_if.connect(env['SSID'], env['PASS'])

while not sta_if.isconnected():
    pass

print(sta_if.ifconfig())