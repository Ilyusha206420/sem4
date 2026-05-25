#pragma once

#include <vector>
#include <fstream>
#include "../model/model.h"

class Parser {
  public:
    Parser(char* filename);
    bool is_open() {return _obj_file.is_open(); };
    void pasre();
  private:
    std::ifstream _obj_file;
    std::vector<Model> _models;
    std::vector<vertex> _vertices;
    std::vector<face> _faces;
};