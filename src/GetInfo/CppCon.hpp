#pragma once


#ifdef _WIN32
  #define CPPCON_EXPORT __declspec(dllexport)
#else
  #define CPPCON_EXPORT
#endif

CPPCON_EXPORT void CppCon();
