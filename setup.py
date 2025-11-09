from setuptools import setup, find_packages

setup(
    name="pylab",  # Replace with your package's name
    version="0.1.0",  # Replace with your package's version
    author="Itay Feldman",  # Replace with your name
    author_email="itayfeldman1@mail.tau.ac.il",  # Replace with your email
    # A brief description
    description="Small package with rather specific functionality tailored for the TAU physics labs",
    # Long description from README.md
    long_description=open("README.md").read(),
    # Specify markdown for long_description
    long_description_content_type="text/markdown",
    # Link to your project's repository
    url="https://github.com/itayf-tau/pylab",
    packages=find_packages(),  # Automatically find all packages in your project
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Or other appropriate license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",  # Minimum Python version required
    install_requires=[
        'scipy',
        'numpy',
        'pandas',
        'matplotlib',
        'dataclasses',
        'typing',
    ],
    extra_require={
        'pandas': ['excel'],
    },
    # Optional: Define entry points for command-line scripts
    # entry_points={
    #     'console_scripts': [
    #         'your_script_name=your_package_name.module:function',
    #     ],
    # },
)
