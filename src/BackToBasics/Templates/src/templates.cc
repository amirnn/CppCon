#include <iostream>

int main() {
  int const &i = 1;
  std::cout << "Here is i: " << i << std::endl;
  return 0;
}