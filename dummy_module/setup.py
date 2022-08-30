from setuptools import Extension, setup
from Cython.Build import cythonize


# setup(
#     ext_modules=cythonize("dummy_module/*.pyx"), #, annotate=True),
# )

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os

packageDir = os.path.dirname(__file__)
includedDir = [packageDir]
os.chdir(packageDir)

ext_modules = [
Extension("dummy_core", ["dummy_core.pyx"], include_dirs=includedDir),
Extension("dummy_utils", ["dummy_utils.pyx"], include_dirs=includedDir)
]

setup(
name='cythonAnimal',
cmdclass={'build_ext': build_ext},
include_dirs=includedDir,
ext_modules=ext_modules,
script_args=['build_ext'],
options={'build_ext':{'inplace':True, 'force':True}}
) 