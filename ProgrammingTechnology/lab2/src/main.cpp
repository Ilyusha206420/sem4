#include <iostream>
#include "./assets/myDouble/myDouble.h"
#include "./assets/myStack/myStack.h"
#include <ctime>
#include <cstdlib>


int main(void)
{
  std::srand(std::time(0));
  myDouble d(double(std::rand()) / (std::rand()), double(std::rand()) / std::rand()); 
  std::cout << "myDouble d = " << d
            << "\n !d = " << !d 
            << "\n d++ = " << d++
            << "\n d-- = " << d--
            << "\n ++d = " << ++d
            << "\n --d = " << --d
            << "\n double(d) = " << double(d) << std::endl;

  myStack s1, s2;
  std::cout << "";
  return 0;
}