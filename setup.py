import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="backupDB",
    version="0.0.1",
    author="Jordan Bell",
    author_email="jb419816@gmail.com",
    description="A somewhat usless package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JD1099/backupDB.git",
    project_urls={
        "Bug Tracker": "https://github.com/JD1099/backupDB/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
