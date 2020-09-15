import os
import re
import glob


def printPackages():
    print('Packages')
    print('========')
    paths = glob.glob(os.path.join('/usr/share', 'cmake*/Modules'))
    modules = [package for path in paths for package in os.listdir(path)]
    [print(module[4:-6]) for module in modules if re.search("^Find", module) and module[4:-6] != '']


def run():
    printPackages()


if __name__ == '__main__':
    run()
