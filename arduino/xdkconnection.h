#define SENSOR_ID_LENGTH 3
#define DATA_LENGTH 25

#define MESSAGE_LENGTH 3
#define PRECISION 65536 // 2 ** 16
#define DELAY 50

#define XDK_OUTPUT_PIN 7
#define XDK_CLOCK_PIN 8

enum SensorId {
  LATITUDE = 2,
  LONGTITUDE = 3,
  TEMPERATURE = 4
};

struct SensorData {
  uint64_t val;
  enum SensorId id;
};

struct SensorData messageContainer[MESSAGE_LENGTH] = {{0, LATITUDE}, {0, LONGTITUDE}, {0, TEMPERATURE}};

/*
 * Message format:
 * HIGH on clock pin (end) -> start message
 * Message format:
 * sensor identifier (SENSOR_ID_LENGTH, lower bits first)
 * number (DATA_LENGTH bits, lower bits first)
 */

void sendBit(bool b) {
  digitalWrite(XDK_OUTPUT_PIN, b);
  delay(DELAY);
}

void sendData(uint64_t val, int n) {
  for (int i = 0; i < n; i++) {
    sendBit(val % 2);
    val /= 2;
  }
}

void startMessage() {
	digitalWrite(XDK_CLOCK_PIN, HIGH);
	delay(DELAY);
	digitalWrite(XDK_CLOCK_PIN, LOW);
}

void send(struct SensorData data) {
	startMessage();
	sendData(data.id, SENSOR_ID_LENGTH);
	sendData(data.val, DATA_LENGTH);
}

uint64_t doubleToMessageVal(double val) {
	return (uint64_t) (val * PRECISION);
}

void sendMessage(size_t start, size_t n) {
	for (size_t i = 0; i < n; i++)
		send(messageContainer[start + i]);
}
