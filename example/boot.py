import network
import config

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

sta_if.connect(config.SSID, config.PASS)

while not sta_if.isconnected():
    pass
print(sta_if.ifconfig())