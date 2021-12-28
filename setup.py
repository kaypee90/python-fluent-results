import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfluent-results",
    url="https://github.com/kaypee90/python-fluent-results",
    author="kaypee90",
    author_email="kaypee90@yahoo.com",
    install_requires=["schema==0.7.5"],
    version="0.0.1",
    license="MIT",
    description="Propagate errors and data nicely with a uniform interface in your python project",
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "fluent_results"},
    packages=setuptools.find_packages(where="fluent_results"),
    python_requires=">=3.6",
)
