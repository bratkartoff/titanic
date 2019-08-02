#include <TinyGPS++.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include "xdkconnection.h"

// GPS
TinyGPSPlus gps;
#define gpsSerial Serial1
#define PMTK_SET_NMEA_UPDATE_1HZ  "$PMTK220,1000*1F"

// Temperature
#define TEMP_SENSOR_PIN 0
OneWire oneWire(TEMP_SENSOR_PIN);
DallasTemperature tempSensor(&oneWire);

void setup() {
  gpsSerial.begin(9600);
  gpsSerial.println(F(PMTK_SET_NMEA_UPDATE_1HZ));
  tempSensor.begin();
}

void updateSensors() {
  while (gpsSerial.available() > 0)
    gps.encode(gpsSerial.read());
    
  tempSensor.requestTemperatures();
}

void transmitData() {
  if (gps.location.isValid()) {
    messageContainer[0].val = doubleToMessageVal(gps.location.lat());
    messageContainer[1].val = doubleToMessageVal(gps.location.lng());
    sendMessage(0, 2);
  }
  messageContainer[2].val = tempSensor.getTempCByIndex(0);
  sendMessage(2, 1);
}

void loop() {
  updateSensors();
  transmitData();
}
