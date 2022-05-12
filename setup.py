from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setup(
        name="pyawscron",
        version="1.0.4",
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
        packages=find_packages(where="src"),
        python_requires=">=3.6",
        install_requires=["python-dateutil~=2.8.1"],
    )
