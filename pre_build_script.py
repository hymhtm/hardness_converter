import os

def modify_cmake_config(cmake_path):
    with open(cmake_path, 'a') as cmake_file:
        cmake_file.write("\n")
        cmake_file.write("set(CMAKE_CXX_STANDARD 20)\n")
        cmake_file.write("set(CMAKE_CXX_STANDARD_REQUIRED ON)\n")

if __name__=="__main__":
    ephemeral_cmake = "./build/windows/ephemeral/CMakeLists.txt"
    if os.path.exists(ephemeral_cmake):
        modify_cmake_config(ephemeral_cmake)
    else:
        print(f"{ephemeral_cmake} not found. Build process might have changed")