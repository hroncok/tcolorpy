import os.path
from typing import Dict

import setuptools


MODULE_NAME = "tcolorpy"
REPOSITORY_URL = f"https://github.com/thombashi/{MODULE_NAME:s}"
REQUIREMENT_DIR = "requirements"

pkg_info: Dict[str, str] = {}


def get_release_command_class() -> Dict[str, setuptools.Command]:
    try:
        from releasecmd import ReleaseCommand
    except ImportError:
        return {}

    return {"release": ReleaseCommand}


with open(os.path.join(MODULE_NAME, "__version__.py")) as f:
    exec(f.read(), pkg_info)

with open("README.rst", encoding="utf8") as f:
    LONG_DESCRIPTION = f.read()

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    TESTS_REQUIRES = [line.strip() for line in f if line.strip()]

setuptools.setup(
    name=MODULE_NAME,
    version=pkg_info["__version__"],
    url=REPOSITORY_URL,
    author=pkg_info["__author__"],
    author_email=pkg_info["__email__"],
    description="tcolopy is a Python library to apply true color for terminal text.",
    include_package_data=True,
    keywords=["ANSI escape", "terminal color", "truecolor"],
    license=pkg_info["__license__"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(exclude=["test*"]),
    package_data={MODULE_NAME: ["py.typed"]},
    project_urls={
        "Source": REPOSITORY_URL,
        "Tracker": f"{REPOSITORY_URL:s}/issues",
    },
    python_requires=">=3.6",
    extras_require={"test": TESTS_REQUIRES},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Text Processing",
    ],
    zip_safe=False,
    cmdclass=get_release_command_class(),
)
