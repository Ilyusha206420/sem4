#include "myStack.h"
#include <ctime>
#include <cstdlib>

stackNode* stackNode::createAndLink(int val)
{
  stackNode* newNode = new stackNode(val, this);
  return newNode;
}

myStack::myStack()
{
  std::srand(std::time(0));
  _size = std::rand() % 14;
  _head = &stackNode(std::rand(), nullptr);
  for (int i = 0; i < _size; i++) 
    _head = _head->createAndLink(std::rand());
}

myStack::~myStack()
{
  stackNode *ptr = _head, *prev = _head->prev();
  while (ptr != nullptr) {
    delete ptr;
    ptr = prev;
    prev = ptr->prev();
  }
}