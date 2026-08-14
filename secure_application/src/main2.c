#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "drone2.h"

int main()
{
    DroneSystem system;

    initializeSystem(&system);

    srand((unsigned int)time(NULL));

    int choice;

    while (1)
    {
        printf("\n");
        printf("====================================\n");
        printf("       DRONE CONTROL SYSTEM\n");
        printf("====================================\n");
        printf("1. Login\n");
        printf("2. Upload Waypoints\n");
        printf("3. Execute Mission\n");
        printf("4. Display Telemetry\n");
        printf("5. View Logs\n");
        printf("6. Exit\n");
        printf("====================================\n");

        printf("Enter choice: ");

        if (scanf("%d", &choice) != 1)
        {
            printf("Invalid input.\n");

            while (getchar() != '\n')
            {
                /* clear input buffer */
            }

            continue;
        }

        switch (choice)
        {
            case 1:
                login(&system);
                break;

            case 2:
                uploadWaypoints(&system);
                break;

            case 3:
                executeMission(&system);
                break;

            case 4:
                displayTelemetry(&system);
                break;

            case 5:
                viewLogs();
                break;

            case 6:
                printf("\nExiting Drone Control System.\n");
                return 0;

            default:
                printf("\nInvalid choice.\n");
        }
    }

    return 0;
}
