import setuptools
import os


version = {}
with open(os.path.abspath("src"+os.path.sep+"pyawscron"+os.path.sep+"version.py")) as fp:
    exec(fp.read(), version)

try:
    assert "." in version['__version__']
except AssertionError:
    raise AssertionError("Failed to obtain version.")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyawscron",
    version=version['__version__'],
    author="Michael Martin",
    author_email="pitchblack408@gmail.com",
    description="An AWS Cron Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pitchblack408/pyawscron",
    project_urls={
        "Bug Tracker": "https://github.com/pitchblack408/pyawscron/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)