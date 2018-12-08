// single DHT 11 temp-humidity sensor on Arduino with serial monitor reporting only
// original written by Tim Stephens 2013 -  http://www.tjstephens.com/blog/2013/11/23/temperature-logger/
// public domain
// modified Floris Wouterlood July 1, 2017

// based on DHT11 examples by Ladyada.
// data pin of DHT11 sensors wired to pin 10 on Arduino
// 10k pull up resistor (between data and 5V)

#include "DHT.h"

float h, t;
DHT DHT_sens(7, DHT11);           //datapin sensor to pin 10 Arduino

int soilMoisture = 0; //value for storing moisture value


int sensorPin = A0;
int sensorValue = 0;
int percent = 0;

void setup()
{

  DHT_sens.begin();

  Serial.begin (9600);
  //   Serial.println ("===============================================");
  //   Serial.println ("Bare DHT11 temp-humidity sensor - June 30, 2017");
  //   Serial.println ("===============================================");
  //   Serial.println (" ");

}

void loop() {
  // ================== read from buffer and display =========================

  h = DHT_sens.readHumidity();
  t = DHT_sens.readTemperature();

  sensorValue = analogRead(sensorPin);
  percent = convertToPercent(sensorValue);

  Serial.print ("H: ");
  Serial.print (h, 2);                 // zero decimal
  Serial.print (" T: ");
  Serial.print (t, 2);                 // one decimal

  Serial.print(" Analog Value: ");
  Serial.print(sensorValue);
  Serial.print(" SM: ");
  Serial.print(percent);
  Serial.println("%");

  // delay of one second
  delay(1000);
}

int convertToPercent(int value)
{
  int percentValue = 0;
  percentValue = map(value, 1023, 350, 0, 100);
  if (percentValue > 100)
    percentValue = 100;
  return percentValue;
}
