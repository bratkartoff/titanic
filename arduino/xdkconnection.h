#define SENSOR_ID_LENGTH 3
#define DATA_LENGTH 25

#define MESSAGE_LENGTH 3
#define PRECISION 65536 // 2 ** 16
#define DELAY 20

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
 * sensor identifier (SENSOR_ID_LENGTH, lower bits first)
 * number (DATA_LENGTH bits, lower bits first)
 * Message format:
 * PREFIX_LENGTH / 4 HIGH
 * PREFIX_LENGTH / 2 LOW
 * PREFIX_LENGTH / 4 HIGH
 * sensor identifier (SENSOR_ID_LENGTH, lower bits first)
 * number (DATA_LENGTH bits, lower bits first)
 */

void sendBit(bool b) {
  digitalWrite(XDK_OUTPUT_PIN, b);
  delay(DELAY);
}

void sendBits(bool b, int n) {
  digitalWrite(XDK_OUTPUT_PIN, b);
  delay(DELAY * n);
}

void sendData(uint64_t val) {
  for (int i = 0; i < DATA_LENGTH; i++) {
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
	sendData(data.id);
	sendData(data.val);
}

uint64_t doubleToMessageVal(double val) {
	return (uint64_t) (val * PRECISION);
}

void sendMessage(size_t start, size_t n) {
	for (size_t i = 0; i < n; i++)
		send(messageContainer[start + i]);
}
