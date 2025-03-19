#include <Arduino_LSM9DS1.h>

void setup() {
    Serial.begin(9600);
    while (!Serial);
    
    if (!IMU.begin()) {
        Serial.println("IMU non détecté !");
        while (1);
    }
    Serial.println("IMU prêt !");
}

void loop() {
    float ax, ay, az, gx, gy, gz;
    
    if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {
        IMU.readAcceleration(ax, ay, az);
        IMU.readGyroscope(gx, gy, gz);
        
        Serial.print("Accélération (m/s²): ");
        Serial.print(ax); Serial.print(", ");
        Serial.print(ay); Serial.print(", ");
        Serial.println(az);

        Serial.print("Gyroscope (°/s): ");
        Serial.print(gx); Serial.print(", ");
        Serial.print(gy); Serial.print(", ");
        Serial.println(gz);
    }

    delay(500);
}
