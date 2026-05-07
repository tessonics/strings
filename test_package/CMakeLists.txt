cmake_minimum_required(VERSION 3.15)

project(example)

add_executable(example src/example.cpp)

find_package(strings REQUIRED CONFIG)
target_link_libraries(example strings::strings)
