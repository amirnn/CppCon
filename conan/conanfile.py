from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class CppConRecipe(ConanFile):
    name = "CppCon"
    version = "1.0"
    package_type = "application"

    # Optional metadata
    license = "MIT"
    author = "Amir Nourinia amir.nouri.nia@gmail.com"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of CppCon package here>"
    topics = ("C++", "Modern C++", "CppCon")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def layout(self):
        cmake_layout(self, src_folder="..", build_folder="../build")

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.user_presets_path = "ConanPresets.json"
        tc.generate()

    def requirements(self):
        self.requires("boost/[~1]")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
