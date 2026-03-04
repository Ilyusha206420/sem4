#include "queue.h"

#include <iostream>
#include <climits>

void Parent::Queue::push(int dat)
{
  _end->data = dat;
  _end->prev = new _queueNode();
  this->_end = _end->prev;
}

int Parent::Queue::pop()
{
  if (!_begin->prev) 
    throw "Attemt to pop from empty queue";
  _queueNode* popedNode = _begin;
  this->_begin = popedNode->prev;
  int res = popedNode->data;
  delete popedNode;
  return res;
}

void Parent::Queue::print()
{
  _queueNode* node = _begin;
  while (node->prev) {
    std::cout << '[' << node->data << "] ";
    node = node->prev;
  }
  std::cout << std::endl;
}

int Parent::Queue::calculateScopeOdd()
{
  int max = INT_MIN, min = INT_MAX;
  _queueNode* node = _begin;
  while (node && node->prev) {
    max = node->data > max ? node->data : max;
    min = node->data < min ? node->data : min;
    std::cout << "Max: " << max << '\n' << "Min " << min << std::endl;
    node = node->prev->prev;
  }
  return max - min;
}

void Parent::Queue::merge(Queue& src)
{
  src._end = this->_end;
  this->_end = _begin;
  while (this->_end->prev->prev)
    this->_end = _end->prev;
  std::cout << _end->data;
  _end->prev = src._begin;
  this->print();
  src._begin = src._end;
}

Parent::Queue::~Queue()
{
  _queueNode* node = _begin;
  _queueNode* prevNode;
  while (node) {
    prevNode = node->prev;
    delete node;
    node = prevNode;
  }
}

Parent::Queue::Queue(const Queue& src) :
_begin(new _queueNode),
_end(_begin)
{
  _queueNode* srcPtr = src._begin;
  while (srcPtr->prev) {
    this->push(srcPtr->data);
    srcPtr = srcPtr->prev;
  }
}
