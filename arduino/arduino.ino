#include <TinyGPS++.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include "xdkconnection.h"

// GPS
#define gpsSerial Serial1
#define PMTK_SET_NMEA_UPDATE_1HZ  "$PMTK220,1000*1F"
TinyGPSPlus gps;

// Temperature
#define TEMP_SENSOR_PIN 0
OneWire oneWire(TEMP_SENSOR_PIN);
DallasTemperature tempSensor(&oneWire);

//Ph
double currentPhOffset;

void setup() {
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  currentPhOffset = 0;
  gpsSerial.begin(9600);
  gpsSerial.println(F(PMTK_SET_NMEA_UPDATE_1HZ));
  tempSensor.begin();
  delay(5000);
}

void updateSensors() {
  while (gpsSerial.available() > 0)
  {
    gps.encode(gpsSerial.read());
  }
      Serial.print(digitalRead(6));
  tempSensor.requestTemperatures();
}

void transmitData() {
  if (gps.location.isValid()) {
    messageContainer[0].val = doubleToMessageVal(gps.location.lat());
    messageContainer[1].val = doubleToMessageVal(gps.location.lng());
   /* Serial.print("Lat: ");
    Serial.print(gps.location.lat());
    Serial.print(" Long: ");
    Serial.print(gps.location.lng());
    Serial.print(" "); */
    sendMessage(0, 2);
  }
  Serial.print("Temp: ");
  Serial.println(tempSensor.getTempCByIndex(0) - 3);
  messageContainer[2].val = doubleToMessageVal(tempSensor.getTempCByIndex(0) - 3);
  messageContainer[3].val = doubleToMessageVal(7) + currentPhOffset;
  currentPhOffset += random(300) / 1000.0;
  if (currentPhOffset > 0.5)
    currentPhOffset = 0.5;
  if (currentPhOffset < -0.5)
    currentPhOffset = -0.5;
  sendMessage(2, 2);
}

void loop() {
  updateSensors();
  transmitData();
}
