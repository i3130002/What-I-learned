/* 
**  Connect the ESP8266 unit to an existing WiFi access point
**  For more information see http://42bots.com
*/

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WiFiMulti.h> 
#include <ESP8266mDNS.h>
#include <ESP8266WebServer.h>   // Include the WebServer library

// Replace these with your WiFi network settings
const char* ssid = "mz"; //replace this with your WiFi network name
const char* password = "12345678"; //replace this with your WiFi network password

void handleRoot();              // function prototypes for HTTP handlers
void handleNotFound();
boolean  led=true;
ESP8266WebServer server(80);    // Create a webserver object that listens for HTTP request on port 80

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT); // initialize digital pin LED_BUILTIN as an output.

  delay(1000);
  Serial.begin(9600);
 
  WiFi.begin(ssid, password);

  Serial.println();
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }

  Serial.println("success!");
  Serial.print("IP Address is: ");
  Serial.println(WiFi.localIP());

  server.on("/", handleRoot);               // Call the 'handleRoot' function when a client requests URI "/"
  server.onNotFound(handleNotFound);        // When a client requests an unknown URI (i.e. something other than "/"), call function "handleNotFound"

  server.begin();                           // Actually start the server
  Serial.println("HTTP server started");
}

void loop() {
    server.handleClient();                    // Listen for HTTP requests from clients
}

void handleRoot() {
  server.send(200, "text/plain", "Hello world!");   // Send HTTP status 200 (Ok) and send some text to the browser/client
  led != led;
  digitalWrite(LED_BUILTIN, led);   // turn the LED on (HIGH is the voltage level)
  Serial.println(led);
}

void handleNotFound(){
  server.send(404, "text/plain", "404: Not found"); // Send HTTP status 404 (Not Found) when there's no handler for the URI in the request
  led = ! led;
  digitalWrite(LED_BUILTIN, led);   // turn the LED on (HIGH is the voltage level)
    Serial.println(led);

  }
