#include <ESP8266WiFi.h> //WiFi library
#include <Wire.h> // I2C library
#include "MAX30105.h" // Heartrate sensor library
#include "heartRate.h" // Heartrate algorithm library

// Pin D4 mapped to pin GPIO2/TXD1 of ESP8266, NodeMCU and WeMoS, control on-board LED
#ifndef LED_BUILTIN
#define LED_BUILTIN 
#endif

volatile uint32_t lastMillis = 0;
MAX30105 particleSensor;
 
const byte RATE_SIZE = 16; //Increase this for more averaging. 4 is good.
byte rates[RATE_SIZE]; //Array of heart rates
byte rateSpot = 0;
long lastBeat = 0; //Time at which the last beat occurred
long irValue = 0;
bool noFinger = false;
float beatsPerMinute;
int beatAvg;
//long rssi = 0;

const char* ssid = "Galaxy A111975";
const char* password = "ftaj6014";
const char* host = "192.168.43.165";
//////////////////////////////////////////////////////////////////////////////////////////

void setup()
{
  Serial.begin(115200);
  Serial.println();
  pinMode(LED_BUILTIN, OUTPUT);
  
  // initialise WiFi client
  Serial.printf("Connecting to %s ", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected to WiFi");

// Initialize sensor
if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) //Use default I2C port, 400kHz speed
{
Serial.println("MAX30105 was not found. Please check wiring/power. ");
while (1);
}
Serial.println("Place your index finger on the sensor with steady pressure.");
 
particleSensor.setup(); //Configure sensor with default settings
particleSensor.setPulseAmplitudeRed(0x0A); //Turn Red LED to low to indicate sensor is running
particleSensor.setPulseAmplitudeGreen(0); //Turn off Green LED
particleSensor.clearFIFO();
}

////////////////////////////////////////////////////////////////////////////////////////////////
void loop()
{  
  WiFiClient client;
  
  Serial.printf("\n[Connecting to %s ... ", host);
  if (client.connect(host, 5000))
  {
    Serial.println("connected to server]");
    digitalWrite(LED_BUILTIN, LOW);
    Serial.println(beatsPerMinute);
    Serial.println(WiFi.RSSI());
    
    // write to wifi Python server
    // We now create a URL for the request. Something like /data/?sensor_reading=123
    String url = "DATA(";
    url += beatsPerMinute;
    url+= ",";
    url += WiFi.macAddress();
    url+= ",";
    url += WiFi.RSSI();
    url+= ",";
    url += noFinger;
    url += ")";

  // This will send the request to the server
    client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" +
               "Connection: close\r\n\r\n");         
  }
  else
  {
    Serial.println("connection to server failed!]");
    digitalWrite(LED_BUILTIN, HIGH);
    client.stop();
  }


/////////////////////////////////////////////////////////////////////////////////////
// get value from sensor
irValue = particleSensor.getIR();

// check to see if finger is on sensor
if (irValue < 50000)
{
  Serial.println("No finger?");
  noFinger = false;
}
else
{
  noFinger = true;
}

if (checkForBeat(irValue) == true)
{
//We sensed a beat!
long delta = millis() - lastBeat;
lastBeat = millis();
 
beatsPerMinute = 60 / (delta / 1000.0);
 
if (beatsPerMinute < 255 && beatsPerMinute > 20)
{
rates[rateSpot++] = (byte)beatsPerMinute; //Store this reading in the array
rateSpot %= RATE_SIZE; //Wrap variable
 
//Take average of readings
beatAvg = 0;
for (byte x = 0 ; x < RATE_SIZE ; x++)
beatAvg += rates[x];
beatAvg /= RATE_SIZE;
client.stop();
    }
  }
}
