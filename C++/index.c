#include <stdio.h>

int main() {
    char fname[20], lname[20];
    printf("What is your first name? : ");
    scanf("%s", fname);

    printf("What is your last name? : ");
    scanf("%s", lname);

    printf("Your fullname is %s and %s.\n", fname, lname);

}