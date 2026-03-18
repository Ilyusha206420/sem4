#pragma once

typedef struct _queueNode {
  int data;
  _queueNode* prev;
  _queueNode(): data(0), prev(nullptr) {};
} _queueNode;

class Queue {
  public:
    void push(int dat);
    int pop();

    void print();
    bool isEmpty() { return !_begin->prev; };
    void merge(Queue& src);
    int calculateScopeOdd();

    Queue(): _begin(new _queueNode()), _end(_begin) {};
    Queue(const Queue& src);
    ~Queue();
  private:
    _queueNode* _begin;
    _queueNode* _end;
  };


namespace Child {
  class publicQueue : public Queue {};

  class protectedQueue : protected Queue {
    public:
      void push(int dat) { Queue::push(dat); };
      int pop() { return Queue::pop(); };
      void print() { Queue::print(); };
      bool isEmpty() { return Queue::isEmpty(); };
      int calculateScopeOdd() { return Queue::calculateScopeOdd(); };
  };

  class privateQueue : private Queue {
    public:
      void push(int dat) { Queue::push(dat); };
      int pop() { return Queue::pop(); };
      void print() { Queue::print(); };
      bool isEmpty() { return Queue::isEmpty(); };
      int calculateScopeOdd() { return Queue::calculateScopeOdd(); };
  };
}
