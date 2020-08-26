import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-react-bridge",
    version="0.0.3",
    author="Giovanni Fumagalli",
    author_email="giovanni.fumagalli@inmagik.com",
    description="A React bridge for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inmagik/django-react-bridge",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests>=2,<3'
    ],
    python_requires='>=3.6',
    include_package_data=True,
)