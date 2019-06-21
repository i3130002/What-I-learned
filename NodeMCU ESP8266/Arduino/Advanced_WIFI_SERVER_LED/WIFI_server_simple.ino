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
const char* ssid = "Been"; //replace this with your WiFi network name
const char* password = "56364626wlan@"; //replace this with your WiFi network password

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

  server.on("/", handleRoot);
  server.on("/on", handleOn);
  server.on("/off", handleOff);
  server.on("/toggle", handleToggle);

  server.onNotFound(handleNotFound);        // When a client requests an unknown URI (i.e. something other than "/"), call function "handleNotFound"

  server.begin();                           // Actually start the server
  Serial.println("HTTP server started");
}

void loop() {
    server.handleClient();                    // Listen for HTTP requests from clients
}

void handleRoot() {
  const char* page = "<html><head> <title>ESP Web Server</title> <meta name='viewport' content='width=device-width, initial-scale=1'>"
"<link rel='icon' href='data:,'> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}"
"h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; "
"border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}"
".button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1>"
"<p>GPIO state: <strong></strong></p><p><button class='button' onclick=\"loadXMLDoc('/on')\">ON</button></p>"
"<p><button class='button button2' onclick=\"loadXMLDoc('/off')\" >OFF</button>"
"<p><button class='button button2' onclick=\"loadXMLDoc('/toggle')\" >Toggle</button></p>"
"</p><div><textarea id='result_viewer' rows='10' cols='50'></textarea></div></body>"
"<script type='text/javascript'>"
"function loadXMLDoc(URL) {"
"    var xmlhttp = new XMLHttpRequest();"
"    xmlhttp.onreadystatechange = function() {"
"        if (xmlhttp.readyState == XMLHttpRequest.DONE) {"
"           if (xmlhttp.status == 200) {"
"               document.getElementById('result_viewer').innerHTML += xmlhttp.responseText;"
"           }"
"           else if (xmlhttp.status == 400) {"
"              alert('There was an error 400');"
"           }"
"           else {"
"               alert('something else other than 200 was returned'+ xmlhttp.readyState);"
"           }"
"        }"
"    };"
"    xmlhttp.open('GET', URL, true);"
"    xmlhttp.send();"
"}"
"</script></html>";
  server.send(200,"text/html", page);   // Send HTTP status 200 (Ok) and send some text to the browser/client
  digitalWrite(LED_BUILTIN, 0);   // turn the LED on (HIGH is the voltage level)
  Serial.println(led);
}

void handleToggle(){
  server.send(200, "text/plain", "Toggled:"+!digitalRead(LED_BUILTIN));
  digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));  
  Serial.println(digitalRead(LED_BUILTIN)+"\n");
}

void handleOn(){
  server.send(200, "text/plain", "TurnedON/n");
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED on (HIGH is the voltage level)
  Serial.println("TurnedON/n");
}
void handleOff(){
  server.send(200, "text/plain", "TurnedOFF/n"); // Send HTTP status 404 (Not Found) when there's no handler for the URI in the request
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED off (LOW is the voltage level)
  Serial.println("TurnedOFF/n");
  }
 void handleNotFound(){
    server.send(404, "text/plain", "Not found"); // Send HTTP status 404 (Not Found) when there's no handler for the URI in the request
    Serial.println("Not found\n");
 }
