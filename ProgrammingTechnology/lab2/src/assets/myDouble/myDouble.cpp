#include "myDouble.h"
#include <ctime>
#include <cstdlib>

myDouble& myDouble::operator++()
{
  _val += _delta;
  return *this;
}

myDouble operator++(const myDouble& obj, int)
{
  std::srand(std::time(0));
  myDouble tmp = myDouble(obj);
  tmp._val += std::rand();
  return tmp;
}

myDouble& myDouble::operator--()
{
  _val -= _delta;
  return *this;
}

myDouble operator--(const myDouble& obj, int)
{
  std::srand(std::time(0));
  myDouble tmp = myDouble(obj);
  tmp._val -= std::rand();
  return tmp;
}

std::ostream& operator<<(std::ostream& os, const myDouble& obj) 
{
  os << obj._val;
  return os;
};
