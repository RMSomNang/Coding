#include <iostream>
#include <string>

int main() {
    int year, age;
    std::cout << "What year did you were born? ";
    std::cin >> year;
    std::cout << "How old are you? ";
    std::cin >> age;
    std::cout << "Hello World. You were born at " << year << ". Your age is " << age << "." << std::endl;
    return 0;
}