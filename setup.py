import codecs
import os
from setuptools import setup, find_packages

dirname = os.path.dirname(__file__)

long_description = (
    codecs.open(os.path.join(dirname, "README.md"), encoding="utf-8").read()
    + "\n"
    + codecs.open(os.path.join(dirname, "CHANGELOG.md"), encoding="utf-8").read()
)

setup(
    name="dp_tools",
    version="rc1.0.6",
    description="Tooling for Data Processing Operations",
    author="Jonathan Oribello",
    author_email="jonathan.d.oribello@nasa.gov",
    packages=find_packages(),  # same as name
    scripts=[],
    package_data={
        "dp_tools": ["config/*.yaml"],
        "dp_tools": ["assets/*"],
    },
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    entry_points={
        "console_scripts": [
            "dpt-get-isa-archive=dp_tools.glds_api.isa:main",
            "dpt-isa-to-runsheet=dp_tools.scripts.convert:main",
        ]
    },
)
