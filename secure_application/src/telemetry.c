#include "drone.h"

void displayTelemetry(void) {
    // Dynamically calculate speed and altitude fluctuation
    int currentSpeed = isFlying ? (40 + (rand() % 15)) : 0;
    
    // Simulate natural battery drain when operating
    if (isFlying && batteryLevel > 5) {
        batteryLevel -= (rand() % 3 + 1);
    }

    printf("\n--- REAL-TIME TELEMETRY DATA ---\n");
    printf("Active Operator: %s\n", operatorName);
    printf("System Status  : %s\n", isFlying ? "IN-FLIGHT / ACTIVE" : "STANDBY / GROUNDED");
    printf("Battery Level  : %d%%\n", batteryLevel);
    printf("Altitude       : %d meters\n", altitudeMeters);
    printf("Speed          : %d km/h\n", currentSpeed);
    printf("Current Target : %s\n", currentWaypoint);
    printf("--------------------------------\n");
}
