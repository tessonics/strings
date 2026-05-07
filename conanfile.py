import os

from conan import ConanFile
from conan.tools.layout import basic_layout
from conan.tools.files import copy
from conan.tools.build import check_min_cppstd

# This conanfile does not rely on CMake and CMake config should care about its own build steps

class StringsConan(ConanFile):
    name = "strings"
    version = "1.0.0"
    package_type = "header-library"

    license = "Tessonics Proprietary License"
    author = "Tessonics Inc."
    url = "https://github.com/tessonics/strings"
    description = "Strings C++ Header-only library"
    topics = ("strings", "header-only", "library")

    exports_sources = "*.hpp"
    no_copy_source = True

    # Needed to define minimum C++ standard
    settings = "compiler"

    # automatically manage the package ID clearing settings and options
    implements = ["auto_header_only"]

    def validate(self):
        check_min_cppstd(self, "20")

    def layout(self):
        basic_layout(self)

    def package(self):
        # Preserve original folder structure: include/strings/header.hpp
        copy(self, "*.hpp", self.source_folder, os.path.join(self.package_folder, "include"))

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
