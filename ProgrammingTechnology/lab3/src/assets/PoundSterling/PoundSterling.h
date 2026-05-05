#pragma ince

#include "../Rouble/Rouble.h"

class PoundSterling: public Rouble
{
  public:
    PoundSterling(): Rouble() {};
    PoundSterling(float val): Rouble(val) {};
    static void setExRate(float exRate) { _exRate = exRate; };
    void print() const override;
    float toRub() const override { return _val * _exRate; };
    void fromRub(float rub) override { _val = rub / _exRate; };
  private:
    static float _exRate;
};