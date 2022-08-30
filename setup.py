from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [
    Extension("dummy_module", ["./dummy_module.pyx"]),
]
setup(
    ext_modules=cythonize(extensions, annotate=True),
)