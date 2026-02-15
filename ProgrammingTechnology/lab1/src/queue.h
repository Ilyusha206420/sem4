#pragma once

typedef struct _queueNode {
  int data;
  _queueNode* prev;
  _queueNode(): data(0), prev(nullptr) {};
} _queueNode;

namespace Parent {

  class Queue {
    public:
      void push(int dat);
      int pop();
      void print();
      bool isEmpty() { return !_begin->prev; };

      Queue(): _begin(new _queueNode()), _end(_begin) {};
      Queue(const Queue& src);
      ~Queue();
    private:
      _queueNode* _begin;
      _queueNode* _end;
  };
}


namespace Child {
  class publicQueue : public Parent::Queue {};

  class protectedQueue : protected Parent::Queue {
    public:
      void push(int dat) { Parent::Queue::push(dat); };
      int pop() { return Parent::Queue::pop(); };
      void print() { Parent::Queue::print(); };
      bool isEmpty() { return Parent::Queue::isEmpty(); };
  };

  class privateQueue : private Parent::Queue {
    public:
      void push(int dat) { Parent::Queue::push(dat); };
      int pop() { return Parent::Queue::pop(); };
      void print() { Parent::Queue::print(); };
      bool isEmpty() { return Parent::Queue::isEmpty(); };
  };
}