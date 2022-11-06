from setuptools import find_packages, setup

with open("README.md") as readme_file:
    README = readme_file.read()

setup_args = dict(
    name="pyFlyway",
    version="0.0.1",
    description="Basic Flyway client written in Python .",
    long_description=README,
    long_description_content_type="text/markdown",
    author="pyCodeBE",
    author_email="pycodeBE@gmail.com",
    license="MIT",
    packages=find_packages(),
    keywords=["Flyway", "database", "migration"],
    url="https://github.com/pycodebe/pyFlyway",
)

install_requires = ["PyYAML"]

if __name__ == "__main__":
    setup(**setup_args, install_requires=install_requires)
