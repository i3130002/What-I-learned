import time
import machine

pin = machine.Pin(2,machine.Pin.OUT)
pin.value(1)
for i in range (0,100):
    time.sleep(0.1)
    pin.value(not pin.value())
