#include <ostream>

struct stackNode {
public:
  int getVal() { return _val; };
  void setVal(int newVal) { _val = newVal; };
  stackNode* prev() { return _prev; };
  stackNode* createAndLink(int val);

  stackNode(): _val(0), _prev(nullptr) {};
  stackNode(int val, stackNode *prev): _val(val), _prev(prev) {};
  stackNode(int val): _val(val), _prev(nullptr) {};

private:
  int _val;
  stackNode *_prev;
};

class myStack {
public:
  friend myStack operator+(const myStack& a, const myStack &b);
  friend myStack operator*(const myStack& a, const myStack& b);
  void operator=(const myStack& other);
  friend myStack operator/(const myStack& a, const myStack& b);
  friend myStack operator-(const myStack& a, const myStack& b);
  void operator+=(const myStack& other);
  void operator*=(const myStack& other);
  void operator/=(const myStack& other);
  void operator-=(const myStack& other);

  int pop();
  void push(int val) { _head = _head->createAndLink(val); _size += 1 ; };

  friend std::ostream& operator<<(std::ostream& os, myStack& stack);

  myStack();
  myStack(const myStack& outher);
  ~myStack();
private:
  stackNode* _head;
  int _size;
};
