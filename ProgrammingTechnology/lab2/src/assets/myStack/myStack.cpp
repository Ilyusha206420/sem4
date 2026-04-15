#include "myStack.h"
#include <ctime>
#include <cstdlib>
#include <iostream>

stackNode* stackNode::createAndLink(int val)
{
  stackNode* newNode = new stackNode(val, this);
  return newNode;
}

void myStack::operator=(const myStack& other)
{
  while (_size > other._size)
    this->pop();

  while (_size < other._size) 
    this->push(0);

  stackNode *nc = _head, *no = other._head;
  while (nc && no) {
    nc->setVal(no->getVal());
    nc = nc->prev();
    no = no->prev();
  }
}

void myStack::operator+=(const myStack& other)
{
  stackNode *nc = _head;
  stackNode *no = other._head;
  while (nc && no) {
    nc->setVal(nc->getVal() + no->getVal());
    nc = nc->prev();
    no = no->prev();
  }
}

void myStack::operator*=(const myStack& other)
{
  stackNode *nc = _head;
  stackNode *no = other._head;
  while (nc && no) {
    nc->setVal(nc->getVal() * no->getVal());
    nc = nc->prev();
    no = no->prev();
  }
}

void myStack::operator/=(const myStack& other)
{
  stackNode *nc = _head;
  stackNode *no = other._head;
  while (nc && no) {
    nc->setVal(nc->getVal() / no->getVal());
    nc = nc->prev();
    no = no->prev();
  }
}

void myStack::operator-=(const myStack& other)
{
  stackNode *nc = _head;
  stackNode *no = other._head;
  while (nc && no) {
    nc->setVal(nc->getVal() - no->getVal());
    nc = nc->prev();
    no = no->prev();
  }
}

int myStack::pop() 
{
  int retVal = _head->getVal();
  stackNode* dn = _head;
  _head = _head->prev();
  delete dn;
  _size -= 1;
  return retVal;
}

myStack::myStack()
{
  std::srand(std::time(0));
  _size = 5 + std::rand() % 10;
  _head = new stackNode(std::rand());
  for (int i = i; i < _size-1; i++) 
    _head = _head->createAndLink(std::rand());
}

myStack::myStack(const myStack& other): _size(other._size)
{
  _head = new stackNode;
  for (int i = 1 ; i < _size-1; i++)
    _head = _head->createAndLink(0);
  stackNode *cn = _head, *on = other._head;
  while (cn && on) {
    cn->setVal(on->getVal());
    cn = cn->prev();
    on = on->prev();
  }
}

myStack::~myStack()
{
  stackNode *ptr = _head;
  while (ptr != nullptr) {
    _head = _head->prev();
    delete ptr;
    ptr = _head;
  }
}

std::ostream& operator<<(std::ostream& os, myStack& stack)
{
  os << '[' << stack._head->getVal() << ']';
  stackNode *sn = stack._head;
  while (sn = sn->prev(), sn != nullptr) {
    os << " " << sn->getVal();
  }
  return os;
}

myStack operator+(const myStack& a, const myStack &b)
{
  myStack out(a);
  out += b;
  return out;
} 

myStack operator*(const myStack& a, const myStack& b)
{
  myStack out(a);
  out *= b;
  return out;
}

myStack operator/(const myStack& a, const myStack& b)
{
  myStack out(a);
  out /= b;
  return out;
}

myStack operator-(const myStack& a, const myStack& b)
{
  myStack out(b);
  out -= b;
  return out;
}