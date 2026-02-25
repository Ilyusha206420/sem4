#include "queue.h"
#include <iostream>
#include <ostream>

int main(int argc, char** argv)
{
  Child::publicQueue queueObj;

  bool running = 1;
  int input = 0;
  while (running) {
    std::cout << "";
    std::cin >> input;
    std::cout << std::endl;
    switch (input) {
      case 1:
        std::cout << "Enter number you want to add: ";
        std::cin >> input;
        queueObj.push(input);
        std::cout << "Number added" << std::endl;
        break;
      case 2:
        if (queueObj.isEmpty())
          std::cout << "Can't pop element from empty queue!" << std::endl;
        else 
          std::cout << "Poped element: " << queueObj.pop() << std::endl;
        break;
      case 3:
        std::cout << "Your queue: " << std::endl;
        queueObj.print();
        break;
      case 4:
        std::cout << "Scope of odd elements in queue: " << queueObj.calculateScopeOdd() << std::endl;
        break;
      case 7:
        running = 0;
        break;
      default:
        break;
    }
  }
  return 0;
}