#ifndef DRONE_H
#define DRONE_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Dynamic Global State
extern int isAuthenticated;
extern char currentWaypoint[32];
extern char operatorName[32];
extern int batteryLevel;
extern int altitudeMeters;
extern int isFlying;

// Function Declarations
void login(void);
void uploadWaypoint(void);
void executeMission(void);
void displayTelemetry(void);
void storeLog(void);

#endif
