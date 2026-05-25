#pragma once 

#include <vector>

struct vertex {
  float x, y, z;
};

struct face {
  int a, b, c;
};

struct Model {
  unsigned int firstVertex;
  unsigned int counrVertices;
  unsigned int firstFace;
  unsigned int countFaces;
};