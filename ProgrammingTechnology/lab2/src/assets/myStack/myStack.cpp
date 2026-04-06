#include "myStack.h"
#include <ctime>
#include <cstdlib>

stackNode* stackNode::createAndLink(int val)
{
  stackNode* newNode = new stackNode(val, this);
  return newNode;
}
