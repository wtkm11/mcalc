"""
Set up measure score project
"""
from setuptools import setup

setup(
    name="mcalc",
    version="1.0",
    py_modules=["mcalc"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    install_requires=[
        "click",  # CLI library
    ],
)
