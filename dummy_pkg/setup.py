from setuptools import Extension, setup

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os

old_dir = os.getcwd()
packageDir = os.path.dirname(__file__)
includedDir = [packageDir]
os.chdir(packageDir)

cython_files = [file for file in os.listdir(".") if file.endswith(".pyx")]
print(f"{len(cython_files)} cython files found ({cython_files})")

ext_modules = [ 
    Extension(cfile.strip(".pyx"), [cfile], include_dirs=includedDir) for cfile in cython_files 
]

setup(
    name=packageDir,
    cmdclass={'build_ext': build_ext},
    include_dirs=includedDir,
    ext_modules=ext_modules,
    script_args=['build_ext'],
    options={'build_ext':{'inplace':True, 'force':True}}
) 
os.chdir(old_dir)