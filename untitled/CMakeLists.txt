cmake_minimum_required(VERSION 3.26)
project(untitled)

set(CMAKE_CXX_STANDARD 17)

add_executable(untitled main.cpp)

include_directories(SFML-2.6.0/include)

target_link_libraries(untitled ${CMAKE_CURRENT_SOURCE_DIR}/SFML-2.6.0/lib/sfml-graphics.lib ${CMAKE_CURRENT_SOURCE_DIR}/SFML-2.6.0/lib/sfml-window.lib ${CMAKE_CURRENT_SOURCE_DIR}/SFML-2.6.0/lib/sfml-system.lib)


