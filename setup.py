from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name="pymop",
    version="0.1.2",
    author="Julian Blank",
    author_email="blankjul@egr.msu.edu",
    description="Optimization Test Problems",
    long_description=readme(),
    url="https://github.com/msu-coinlab/pymop",
    license='MIT',
    keywords="optimization",
    packages=['pymop'],
    install_requires=['numpy', 'matplotlib', 'scipy']
)
