import setuptools
from ptmethods._version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ptmethods",
    version=__version__,
    description="HTTP methods testing tool",
    author="Penterep",
    author_email="info@penterep.com",
    url="https://www.penterep.com/",
    license="GPLv3+",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Environment :: Console",
        "Topic :: Security",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
    ],
    python_requires='>=3.6',
    install_requires=["ptlibs>=1,<2", "requests"],
    entry_points = {'console_scripts': ['ptmethods = ptmethods.ptmethods:main']},
    long_description=long_description,
    long_description_content_type="text/markdown",
)