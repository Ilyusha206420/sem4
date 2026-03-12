#include "../src/queue.h"

#include <iostream>

int main() 
{
  Child::publicQueue test;
  test.push(-3);
  test.push(-8);
  test.push(-13);
  test.push(-80);
  test.push(-130);
  std::cout << test.calculateScopeOdd() << std::endl;
}