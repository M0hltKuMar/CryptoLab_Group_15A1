#include "drone.h"

void executeMission(void) {
    // VULNERABILITY 1: Missing Authentication Check
    // (Notice: 'isAuthenticated' is not checked before proceeding)

    char host[64];
    char command[128];

    printf("\n[!] Initializing Mission for Target Coordinates: %s\n", currentWaypoint);
    printf("Enter Drone Communications Link Host/IP for pre-flight ping: ");
    scanf("%63s", host);

    printf("[*] Running pre-flight diagnostic...\n");

    // VULNERABILITY 2: Command Injection
    // Flawfinder flags 'sprintf' and 'system'
    sprintf(command, "ping -c 1 %s", host); 
    system(command); 

    // Update dynamic operational states upon successful mission launch
    isFlying = 1;
    altitudeMeters = 100 + (rand() % 80); // Dynamic altitude between 100-180m
    if (batteryLevel > 10) batteryLevel -= 5;

    printf("[+] Mission Executed Successfully! Drone deployed to %dm altitude.\n", altitudeMeters);
}
