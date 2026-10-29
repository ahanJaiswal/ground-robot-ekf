cmake_minimum_required(VERSION 3.16)
project(ground_robot_ekf VERSION 0.1.0 LANGUAGES CXX)

add_executable(ground_robot_ekf
    src/main.cpp
    src/csv_reader.cpp
    src/dead_reckoning.cpp
)
target_compile_features(ground_robot_ekf PRIVATE cxx_std_17)
set_target_properties(ground_robot_ekf PROPERTIES CXX_EXTENSIONS OFF)
target_include_directories(ground_robot_ekf PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    target_compile_options(ground_robot_ekf PRIVATE -Wall -Wextra -Wpedantic)
endif()
