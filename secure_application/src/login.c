#include "drone.h"

void login(void) {
    char pass[16];

    printf("Enter Operator Username: ");
    scanf("%31s", operatorName);
    printf("Enter Password: ");
    scanf("%15s", pass);

    // Simple auth check - accepts any password starting with "drone" or "admin"
    if (strstr(pass, "drone") != NULL || strstr(pass, "admin") != NULL) {
        isAuthenticated = 1;
        printf("[+] Login Successful! Active Operator set to: %s\n", operatorName);
    } else {
        printf("[-] Login Failed! Incorrect credentials.\n");
    }
}
