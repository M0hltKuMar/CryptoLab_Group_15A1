#include "drone.h"

void storeLog(void) {
    char logFilePath[128];
    FILE *file;
    time_t rawtime;
    struct tm *timeinfo;

    // Fetch current system timestamp dynamically
    time(&rawtime);
    timeinfo = localtime(&rawtime);

    printf("Enter log file path/filename to save (e.g., flight.log): ");
    scanf("%127s", logFilePath);

    // VULNERABILITY 3: Insecure File Handling / Path Traversal
    // Flawfinder flags 'fopen'
    file = fopen(logFilePath, "w"); 
    if (file == NULL) {
        printf("[-] Log Storage Error: Unable to open file.\n");
        return;
    }

    // Writes real dynamic data instead of hardcoded strings
    fprintf(file, "=== DRONE TELEMETRY LOG ===\n");
    fprintf(file, "Timestamp      : %s", asctime(timeinfo));
    fprintf(file, "Operator       : %s\n", operatorName);
    fprintf(file, "Flight Status  : %s\n", isFlying ? "IN-FLIGHT" : "STANDBY");
    fprintf(file, "Target Coords  : %s\n", currentWaypoint);
    fprintf(file, "Battery Level  : %d%%\n", batteryLevel);
    fprintf(file, "Altitude       : %d meters\n", altitudeMeters);
    fprintf(file, "===========================\n");
    fclose(file);

    printf("[+] Telemetry log saved successfully to: %s\n", logFilePath);
}
