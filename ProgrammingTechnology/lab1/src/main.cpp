#include "queue.h"
#include <cstring>
#include <iostream>

int main(int argc, char** argv)
{
  if (argc == 2) {
    if (strcmp(argv[1], "-private")) {
      Child::privateQueue queueObj;
    } else if (strcmp(argv[1], "-protected")) {
      Child::protectedQueue queueObj;
    } else if (strcmp(argv[1], "-public")) {
      Child::publicQueue queueObj;
    } else {
      Child::publicQueue queueObj;
    }
  } else {
    Child::publicQueue queueObj;
  }

  bool running = 1;
  int input = 0;
  while (running) {
    std::cout << "";
    std::cin >> input;
    std::cout << std::endl;
    switch (input) {
      case 0:
        running = 0;
        break;
      default:
        break;
    }
  }
  return 0;
}