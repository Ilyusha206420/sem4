class myDouble {
  public:
    void operator++();
    void operator++(int);
    void operator--();
    void operator--(int);
    
  private:
    double _val;
};