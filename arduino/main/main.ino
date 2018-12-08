#include "DHT.h"                  // Include library for DHT humidity and temperature sensor

float h, t;
DHT DHT_sens(7, DHT11);           // Datapin sensor to pin 7 Arduino

int soilMoisture = 0;             // Storing Moisture value
int sensorValue = 0;
int percentSoilMoist = 0;         // Soil Moisture value in percents

int DHTPin = A0;                  // DHT at Arduino analog pin A0
int resistorPin = A1;             // Photoresistor at Arduino analog pin A1

void setup(){
  DHT_sens.begin();
  Serial.begin (9600);
}

void loop() {
  // ================== read from buffer and display =========================
  h = DHT_sens.readHumidity();
  t = DHT_sens.readTemperature();

  //TODO: extract two lines below in a method to return a single value 
  sensorValue = analogRead(DHTPin);
  percentSoilMoist = convertToPercent(sensorValue);
  
  send_data();

  // delay of one second
  delay(1000);
}

void send_data(){
  Serial.print ("H:");             // Humidity
  Serial.print (h);                 // Printing humidity value from DHT sensor
  Serial.print (" T:");            // Temperature
  Serial.print (t);                 // Printing temperature value from DHT sensor

  Serial.print(" SMV:");
  Serial.print(sensorValue);
  Serial.print(" SMP:");            // Soil Moisture 
  Serial.print(percentSoilMoist);   // Printing Soil Moisture value in percents from Soil Moisture sensor
  Serial.print("%");

  Serial.print(" SL:"); // Sunlight value
  Serial.println(analogRead(resistorPin)); // Printing Sunlight value from photoresistor
}

int convertToPercent(int value)
{
  int percentValue = 0;
  percentValue = map(value, 1023, 350, 0, 100);

  if (percentValue > 100)
    percentValue = 100;
  return percentValue;
}
