#include <stdio.h>
#include <string.h>
#include "drone2.h"

void initializeSystem(DroneSystem *system)
{
    system->loggedIn = 0;
    system->username[0] = '\0';
    system->waypointCount = 0;
    system->missionActive = 0;
}

int login(DroneSystem *system)
{
    char username[50];
    char password[50];

    printf("\n===== DRONE LOGIN =====\n");

    printf("Username: ");
    scanf("%49s", username);

    printf("Password: ");
    scanf("%49s", password);

    if (strcmp(username, "admin") == 0 &&
        strcmp(password, "admin123") == 0)
    {
        system->loggedIn = 1;

        snprintf(system->username,
                 sizeof(system->username),
                 "%s",
                 username);

        printf("\nLogin successful!\n");

        return 1;
    }

    printf("\nInvalid username or password.\n");

    return 0;
}

void uploadWaypoints(DroneSystem *system)
{
    int count;

    printf("\n===== UPLOAD WAYPOINTS =====\n");

    printf("Enter number of waypoints: ");
    scanf("%d", &count);

    if (count <= 0 || count > MAX_WAYPOINTS)
    {
        printf("Invalid number of waypoints.\n");
        return;
    }

    system->waypointCount = count;

    for (int i = 0; i < count; i++)
    {
        printf("\nWaypoint %d\n", i + 1);

        printf("Latitude: ");
        scanf("%f", &system->waypoints[i].latitude);

        printf("Longitude: ");
        scanf("%f", &system->waypoints[i].longitude);
    }

    printf("\nWaypoints uploaded successfully.\n");
}

void executeMission(DroneSystem *system)
{
    printf("\n===== MISSION EXECUTION =====\n");

    if (system->waypointCount == 0)
    {
        printf("No waypoints uploaded.\n");
        return;
    }

    system->missionActive = 1;

    printf("Mission started.\n");

    for (int i = 0; i < system->waypointCount; i++)
    {
        printf("Drone moving to waypoint %d "
               "(%.4f, %.4f)\n",
               i + 1,
               system->waypoints[i].latitude,
               system->waypoints[i].longitude);
    }

    system->missionActive = 0;

    printf("Mission completed.\n");
}

void displayTelemetry(DroneSystem *system)
{
    printf("\n===== DRONE TELEMETRY =====\n");

    printf("Status     : %s\n",
           system->missionActive ? "ACTIVE" : "IDLE");

    printf("Altitude   : 120 m\n");
    printf("Speed      : 35 km/h\n");
    printf("Battery    : 82%%\n");

    if (system->waypointCount > 0)
    {
        printf("Latitude   : %.4f\n",
               system->waypoints[0].latitude);

        printf("Longitude  : %.4f\n",
               system->waypoints[0].longitude);
    }
    else
    {
        printf("Latitude   : N/A\n");
        printf("Longitude  : N/A\n");
    }
}

void viewLogs(void)
{
    FILE *file = fopen("../outputs/logs.txt", "r");

    if (file == NULL)
    {
        printf("\nNo log file found.\n");
        return;
    }

    char line[200];

    printf("\n===== DRONE LOGS =====\n");

    while (fgets(line, sizeof(line), file))
    {
        printf("%s", line);
    }

    fclose(file);
}
