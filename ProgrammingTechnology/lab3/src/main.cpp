#include "assets/Currencies.h"


#include <iostream>

int main()
{
  float input = 0;

  std::cout << "Enter Dollar in Roubles: ";
  std::cin >> input;
  Dollar::setExRate(input);

  std::cout << "Enter quantity of Dollars: ";
  std::cin >> input;
  Dollar d(input);

  std::cout << "Enter Euri in Roubles: ";
  std::cin >> input;
  Euro::setExRate(input);

  std::cout << "Enter quantity of Euros: ";
  std::cin >> input;
  Euro e(input);

  std::cout << "Enter Japanese Yen in Roubles: ";
  std::cin >> input;
  JapaneseYen::setExRate(input);

  std::cout << "Enter quantity of Japanese Yens: ";
  std::cin >> input;
  JapaneseYen jy(input);

  std::cout << "Enter Pound Sterling in Roubles: ";
  std::cin >> input;
  PoundSterling::setExRate(input);

  std::cout << "Enter quantity of Pounds Sterling: ";
  std::cin >> input;
  PoundSterling ps(input);

  std::cout << "You entered: " << std::endl;
  d.print();
  e.print();
  jy.print();
  ps.print();

  std::cout << "In Roubles it is: \nDollars: " << d.toRub() 
            << "\nEuros: " << e.toRub()
            << "\nJapanese Yens: " << jy.toRub()
            << "\nPounds Sterling: " << ps.toRub()
            << std::endl; 
  return 0;
}