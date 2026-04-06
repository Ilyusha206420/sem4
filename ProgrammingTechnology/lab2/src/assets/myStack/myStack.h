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
  myStack();
  ~myStack();
private:
  stackNode* _head;
  int _size;
};