#include "Currencies.h"

#include <iostream>

float Dollar::_exRate = 0;
void Dollar::print() const
{
  std::cout << _val << " $" << std::endl;
}

float Euro::_exRate = 0;
void Euro::print() const
{
  std::cout << _val << " E" << std::endl;
}

float JapaneseYen::_exRate = 0;
void JapaneseYen::print() const
{
  std::cout << _val << " JY" << std::endl;
}

float PoundSterling::_exRate = 0;
void PoundSterling::print() const
{
  std::cout << _val << " PS" << std::endl;
}