cmake_minimum_required(VERSION 3.13)
project(STRUMPACK-example VERSION 0.1 LANGUAGES CXX)

find_package(STRUMPACK REQUIRED)

add_executable(testHODLR            testHODLR.cpp)
add_executable(testPoisson3d        testPoisson3d.cpp)
add_executable(testPoisson3dMPIDist testPoisson3dMPIDist.cpp)
add_executable(testMMdouble         testMMdouble.cpp)
add_executable(testMMdoubleMPIDist  testMMdoubleMPIDist.cpp)

target_link_libraries(testHODLR            PRIVATE STRUMPACK::strumpack)
target_link_libraries(testPoisson3d        PRIVATE STRUMPACK::strumpack)
target_link_libraries(testPoisson3dMPIDist PRIVATE STRUMPACK::strumpack)
target_link_libraries(testMMdouble         PRIVATE STRUMPACK::strumpack)
target_link_libraries(testMMdoubleMPIDist  PRIVATE STRUMPACK::strumpack)
