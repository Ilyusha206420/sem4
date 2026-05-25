#include <iostream>
#include "./assets/myDouble/myDouble.h"

int main(void)
{
  myDouble a(1, 2);
  ++a;
  std::cout << a << std::endl;
  --a;
  std::cout << a << std::endl;
  std::cout << a++ << std::endl;
  std::cout << a-- << std::endl;
  return 0;
}