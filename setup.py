from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="python_library_sample",
    version="0.1.0",
    # license="ライセンス",
    description="Description Here",
    author="Author Here",
    # author_email="contact@ryo1999.com",
    url="https://github.com/ryofujimotox/python_library_sample",
    # packages=find_packages(),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=_requires_from_file("requirements.txt"),
    include_package_data=True,
)
