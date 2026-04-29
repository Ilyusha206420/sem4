#pragma once

class Rouble
{
  public:
    Rouble(): _val(0) {}; 
    Rouble(float val): _val(val) {} ;
    void set(float newVal) { _val = newVal; };
    float get() { return _val; };
    virtual void print() const = 0;
    virtual float toRub() const = 0;
    virtual void fromRub(float rub) = 0;
  protected:
    float _val;
};