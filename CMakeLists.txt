cmake_minimum_required(VERSION 3.23)

project(strings)

set(LIBRARY_NAME strings)

add_library(${LIBRARY_NAME} INTERFACE)
target_compile_features(${LIBRARY_NAME} INTERFACE cxx_std_20)
target_compile_definitions(${LIBRARY_NAME} INTERFACE LIBCXX_ENABLE_INCOMPLETE_FEATURES)

if(CMAKE_CXX_COMPILER_ID STREQUAL "AppleClang")
    target_compile_definitions(strings INTERFACE
        STRINGS_USE_TOCHARS_FLOAT_STUB
        STRINGS_APPLE_CLANG_RANGES)
endif()

file(GLOB_RECURSE HEADERS strings/*.hpp)
target_sources(${LIBRARY_NAME}
  INTERFACE
    FILE_SET HEADERS # since CMake 3.23
    FILES
      ${HEADERS}
)

install(TARGETS ${LIBRARY_NAME} FILE_SET HEADERS)
