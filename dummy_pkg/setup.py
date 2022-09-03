from setuptools import Extension, setup
import os
import argparse
from Cython.Distutils import build_ext
from Cython.Compiler.Options import get_directive_defaults

from rich import print

parser = argparse.ArgumentParser()
parser.add_argument('--profile', action='store_true')

# Set the working directory
old_dir = os.getcwd()
packageDir = os.path.dirname(__file__)
includedDir = [packageDir]
os.chdir(packageDir)

extension_kwargs = dict( 
        include_dirs=includedDir,
        libraries=["m"],                # Unix-like specific link to C math libraries
        extra_compile_args=["-fopenmp"],# Links OpenMP for parallel computing
        extra_link_args=["-fopenmp"],
        )
# Profiling using line_profiler
if parser.parse_args().profile:
    print("[blue]Compiling in profiler mode[/blue]")
    directive_defaults = get_directive_defaults()
    directive_defaults['linetrace'] = True
    directive_defaults['binding'] = True
    # Activates profiling
    extension_kwargs["define_macros"] = [('CYTHON_TRACE', '1'), ('CYTHON_TRACE_NOGIL', '1')]

# Finds each .pyx file and adds it as an extension
cython_files = [file for file in os.listdir(".") if file.endswith(".pyx")]
print(f"{len(cython_files)} cython files found ({cython_files})")
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

# Sets back working directory to old one
os.chdir(old_dir)
