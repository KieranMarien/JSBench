import os
import shutil
import subprocess

def find_package_json_files(path):
    """
    Recursively find all package.json files in the given directory and its subdirectories.
    Returns a list of absolute file paths.
    """
    package_json_files = []
    for root, dirs, files in os.walk(path):
        if "package.json" in files:
            package_json_files.append(os.path.abspath(os.path.join(root, "package.json")))
    return package_json_files

def install_packages():
    """
    Recursively find every package.json file in the current directory and its subdirectories,
    and run npm i in each directory that contains a package.json file.
    """
    package_json_files = find_package_json_files(".")
    for package_json_file in package_json_files:
        directory = os.path.dirname(package_json_file)
        print(f"Installing packages in {directory}")
        subprocess.run(["npm", "i"], cwd=directory)

if __name__ == '__main__':
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            if name == "node_modules":
                shutil.rmtree(os.path.join(root, name))
    install_packages()
