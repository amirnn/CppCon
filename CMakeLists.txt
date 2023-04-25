cmake_minimum_required(VERSION 3.26.3)
project(CppCon CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(EXPORT_COMPILE_COMMANDS True)

include("conan/dependencies.cmake")

add_subdirectory("src/BackToBasics/Templates")
add_subdirectory("src/main")
