/* 
**  Connect the ESP8266 unit to an existing WiFi access point
**  For more information see http://42bots.com
*/

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WiFiMulti.h> 
#include <ESP8266mDNS.h>
#include <ESP8266WebServer.h>   // Include the WebServer library

ESP8266WebServer server(80);    // Create a webserver object that listens for HTTP request on port 80

void setup()
{
   WiFi.mode( WIFI_OFF );
   WiFi.forceSleepBegin();
}

void loop() {
delay(100000);
}
