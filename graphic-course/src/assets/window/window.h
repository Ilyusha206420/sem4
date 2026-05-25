#pragma once
#include <GL/glew.h>
#include <GLFW/glfw3.h>

class Window {
    Window(char* filename);
    ~Window() { glfwTerminate(); };
    bool check() { return _window != NULL; };
    bool initGlew();
    void adapt();
    bool close() { return glfwWindowShouldClose(_window); };
  private:
    GLFWwindow* _window;
    int _height;
    int _width;
};