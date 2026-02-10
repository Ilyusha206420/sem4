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

    Queue(): _begin(new _queueNode()), _end(_begin) {};
    Queue(const Queue& src);
    ~Queue();
  private:
    _queueNode* _begin;
    _queueNode* _end;
};