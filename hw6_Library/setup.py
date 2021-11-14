from setuptools import setup, find_packages

def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]

setup(
    name='data_analysis',
    version='0.1',
    description='',
    author='',
    packages=find_packages(exclude=['tests']),
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    url='',
    classifiers=[
        'Programming Language :: Python :: 3.8'
    ]
)
