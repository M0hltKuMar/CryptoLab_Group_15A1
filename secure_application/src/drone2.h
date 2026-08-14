#ifndef DRONE2_H
#define DRONE2_H

#define MAX_WAYPOINTS 20

typedef struct
{
    float latitude;
    float longitude;
} Waypoint;

typedef struct
{
    int loggedIn;
    char username[50];

    Waypoint waypoints[MAX_WAYPOINTS];
    int waypointCount;

    int missionActive;
} DroneSystem;

void initializeSystem(DroneSystem *system);

int login(DroneSystem *system);

void uploadWaypoints(DroneSystem *system);

void executeMission(DroneSystem *system);

void displayTelemetry(DroneSystem *system);

void viewLogs(void);

#endif
