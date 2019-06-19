try:
  import usocket as socket
except:
  import socket
from machine import Pin
import network


def web_page():
  if led.value() == 1:
    gpio_state="OFF"
  else:
    gpio_state="ON"
  
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/on"><button class="button">ON</button></a></p>
  <p><a href="/off"><button class="button button2">OFF</button></a></p></body></html>"""
  return html

def notify_led_change(led_status):
    host = "192.168.1.100"
    print("sending get to slave")
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (led_status, host), 'utf8'))
    s.close()

led = Pin(2, Pin.OUT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(50)

while True:
  conn, addr = s.accept()
#   print('Got a connection from %s' % str(addr))
  request = conn.recv(1024*5)
  request = str(request)
#   print('Content = %s' % request)
  led_on = request.find('/on')
  led_off = request.find('/off')
  if led_on == 6:
    print('ON')
    led.value(0)
    # notify_led_change("on")
  if led_off == 6:
    print('OFF')
    led.value(1)
    # notify_led_change("off")
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

