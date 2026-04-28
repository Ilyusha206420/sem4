#include "assets/Currencies.h"

#include <iostream>

int main()
{
  float input = 0;
  std::cout << "Enter Dollar exchange rate: ";
  std::cin >> input;
  Dollar::setExRate(input);

  std::cout << "Enter Euro exchange rate: ";
  std::cin >> input;
  Euro::setExRate(input);

  std::cout << "Enter Japanese Yen exchange rate: ";
  std::cin >> input;
  JapaneseYen::setExRate(input);
  
  std::cout << "Enter Pound Sterling exchange rate: ";
  std::cin >> input;
  PoundSterling::setExRate(input);
  
  return 0;
}