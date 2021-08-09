from setuptools import setup
with open('requirements.txt') as f:
    required = f.read().splitlines()
setup(
    name='application',
    packages=['application'],
    include_package_data=True,
    install_requires=[
        required
    ],
)
