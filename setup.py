import setuptools
import subprocess
import os

version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
        .stdout.decode("utf-8")
        .strip()
)

assert "." in version
with open("src/pyawscron/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{version}\n")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyawscron-pitchblack408",
    version=version,
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