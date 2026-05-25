#include "parser.h"
#include <sstream>
#include <string>
#include <vector>

Parser::Parser(char* filename) 
{
  std::ifstream _obj_file(filename);
  std::vector<Model> _models;
  std::vector<vertex> _vertices;
  std::vector<face> _faces;
}

void Parser::pasre()
{
  std::string line;
  while (std::getline(_obj_file, line))
  {
    if (line.empty()) continue;
    std::stringstream ss(line);
    std::string type;
    ss >> type;
    if (type == "#") continue;
    else if (type == "v") {
      float x, y, z;
      ss >> x >> y >> z;
      _vertices.push_back({x, y, z});
    } else if (type == "f") {
      std::vector<int> vert_ind;
      std::string vert_data;
      while (ss >> vert_data) 
      {
        std::stringstream vert_ss(vert_data);
        int ind;
      }
    } else continue;
  }
}
