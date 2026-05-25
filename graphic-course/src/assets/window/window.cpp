#include "window.h"
#include <GL/gl.h>
#include <GLFW/glfw3.h>
#include <cstddef>

void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
  glViewport(0, 0, width, height);
}

Window::Window(char* filename)
{
  glfwInit();
  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
  glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
  _window = glfwCreateWindow(600, 400, filename, NULL, NULL);
}

bool Window::initGlew() 
{
  glewExperimental = true;
  return glewInit() == GLEW_OK;
}

void Window::adapt() 
{
  glfwSetFramebufferSizeCallback(_window, framebuffer_size_callback);
  glfwMakeContextCurrent(_window);
  glfwGetFramebufferSize(_window, &_width, &_height);
  glViewport(0, 0, _width, _height);
}