from setuptools import setup

setup(
    name="Python Fluent Results",
    url="https://github.com/kaypee90/python-fluent-results",
    author="kaypee90",
    author_email="kaypee90@yahoo.com",
    packages=["fluent_results"],
    install_requires=["schema==0.7.5"],
    version="0.0.1",
    license="MIT",
    description="Propagate errors and data nicely with a uniform interface in your python project",
    long_description=open("README.md").read(),
    python_requires=">=3.6",
)