#include "queue.h"

#include <iostream>

void Queue::push(int dat)
{
  _end->data = dat;
  _end->prev = new _queueNode();
  this->_end = _end->prev;
}

int Queue::pop()
{
  if (!_begin->prev) 
    throw "Attemt to pop from empty queue";
  _queueNode* popedNode = _begin;
  this->_begin = popedNode->prev;
  int res = popedNode->data;
  delete popedNode;
  return res;
}

void Queue::print()
{
  _queueNode* node = _begin;
  while (node->prev) {
    std::cout << '[' << node->data << "] ";
    node = node->prev;
  }
  std::cout << std::endl;
}

Queue::~Queue()
{
  _queueNode* node = _begin;
  _queueNode* prevNode;
  while (node) {
    prevNode = node->prev;
    delete node;
    node = prevNode;
  }
}

Queue::Queue(const Queue& src) :
_begin(new _queueNode),
_end(_begin)
{
  _queueNode* srcPtr = src._begin;
  while (srcPtr->prev) {
    this->push(srcPtr->data);
    srcPtr = srcPtr->prev;
  }
}