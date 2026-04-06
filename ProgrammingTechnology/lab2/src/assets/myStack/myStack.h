struct stackNode {
public:
  int getVal() { return _val; };
  void setVal(int newVal) { _val = newVal; };
  stackNode* prev() { return _prev; };
  
private:
  int _val;
  stackNode* _prev;
};

class myStack {
public:
  myStack();
  ~myStack();
private:

};