#include "drone.h"

void uploadWaypoint(void) {
    char inputBuffer[256];
    printf("Enter Waypoint Coordinates (Lat, Long): ");
    scanf(" %[^\n]s", inputBuffer); 

    // VULNERABILITY 4: Buffer Overflow
    // Flawfinder flags 'strcpy'
    strcpy(currentWaypoint, inputBuffer); 

    printf("[+] New Waypoint successfully uploaded: %s\n", currentWaypoint);
}
