from time import sleep
from rpi_TM1638 import TMBoards
import paho.mqtt.publish as publish

STB = 14
CLK = 15
DIO = 18
mqtt_topic = 'ITTEK'
mqtt_server = 'test.mosquitto.org'
TM = TMBoards(DIO, CLK, STB, 0)
TM.clearDisplay()


def sendingthings():
        while True:
            for i in range(8):
                
                publish.single(mqtt_topic, i, hostname= mqtt_server) if TM.switches[i] else False
    
def buttonpushing():
    TM.leds[0] = True
    while True:
        for i in range(8):
            TM.leds[i] = True if TM.switches[i] else False
            if TM.switches[i]:
                publish.single(mqtt_topic, i , hostname = mqtt_server)
                sleep(0.5)

def username():
    TM.segments[0] = 'User'
    TM.segments[4] = '1'

username()

buttonpushing()

