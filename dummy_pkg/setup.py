from setuptools import Extension, setup
from Cython.Distutils import build_ext
import os

# Profiling stuff
from Cython.Compiler.Options import get_directive_defaults

directive_defaults = get_directive_defaults()

directive_defaults['linetrace'] = True
directive_defaults['binding'] = True

# Set the working directory
old_dir = os.getcwd()
packageDir = os.path.dirname(__file__)
includedDir = [packageDir]
os.chdir(packageDir)

cython_files = [file for file in os.listdir(".") if file.endswith(".pyx")]
print(f"{len(cython_files)} cython files found ({cython_files})")

extension_kwargs = dict( 
        include_dirs=includedDir,
        libraries=["m"],                # Unix-like specific link to C math libraries
        extra_compile_args=["-fopenmp"],# Links OpenMP for parallel computing
        extra_link_args=["-fopenmp"],
        )

# Activates profiling
extension_kwargs["define_macros"] = [('CYTHON_TRACE', '1'), ('CYTHON_TRACE_NOGIL', '1')]

ext_modules = [
    Extension(
        cfile.strip(".pyx"),
        [cfile],
        **extension_kwargs
    )
    for cfile in cython_files
]

setup(
    name=packageDir,
    cmdclass={"build_ext": build_ext},
    include_dirs=includedDir,
    ext_modules=ext_modules,
    script_args=["build_ext"],
    options={"build_ext": {"inplace": True, "force": True}},
)
os.chdir(old_dir)
