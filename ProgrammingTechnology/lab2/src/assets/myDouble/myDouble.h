#include <ostream>

class myDouble {
  public:
    myDouble& operator++();
    friend myDouble operator++(const myDouble& obj, int);
    myDouble& operator--();
    friend myDouble operator--(const myDouble& obj, int);
    
    myDouble operator !() { return myDouble(-_val, _delta); };

    friend std::ostream& operator<<(std::ostream& os, const myDouble& obj);

    explicit operator double() const { return _val; };

    void setDelta(double newDelta) { _delta = newDelta; };
    
    myDouble(const myDouble& other): _val(other._val), _delta(other._delta) {};
    myDouble(double value, double delta): _val(value), _delta(delta) {};
    myDouble(): _val(0), _delta(0) {};
  private:
    double _val;
    double _delta;
};