cmake_minimum_required(VERSION 3.9)

project(cmake_task)

find_package(PythonInterp 3 REQUIRED)
execute_process(COMMAND ${PYTHON_EXECUTABLE} A/preparing.py WORKING_DIRECTORY ${PROJECT_SOURCE_DIR} )

include_directories(A B)
add_subdirectory(B)

add_executable(main C/main.cpp)

target_link_libraries(main lib)
