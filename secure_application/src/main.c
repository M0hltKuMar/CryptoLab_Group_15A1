#include "drone.h"

// Initialize Dynamic State Variables
int isAuthenticated = 0;
char currentWaypoint[32] = "37.7749, -122.4194"; // Default SF coordinates
char operatorName[32] = "GUEST";
int batteryLevel = 100;
int altitudeMeters = 0;
int isFlying = 0;

int main(void) {
    char choice[10];
    srand(time(NULL)); // Seed random number generator for realistic telemetry

    while (1) {
        printf("\n=================================\n");
        printf("   DRONE CONTROL SYSTEM (v2.0)   \n");
        printf("=================================\n");
        printf("1. Drone Login\n");
        printf("2. Waypoint Upload\n");
        printf("3. Mission Execution\n");
        printf("4. Telemetry Display\n");
        printf("5. Log Storage\n");
        printf("6. Exit\n");
        printf("Select an option (1-6): ");

        if (scanf("%9s", choice) != 1) break;

        switch (choice[0]) {
            case '1': login(); break;
            case '2': uploadWaypoint(); break;
            case '3': executeMission(); break;
            case '4': displayTelemetry(); break;
            case '5': storeLog(); break;
            case '6':
                printf("[+] Exiting system... Goodbye.\n");
                return 0;
            default:
                printf("[-] Invalid option. Please try again.\n");
        }
    }
    return 0;
}
