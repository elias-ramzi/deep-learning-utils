import setuptools

with open('requirements.txt') as open_file:
    install_requires = open_file.read()

setuptools.setup(
    name='dlu',
    version='0.0.0',
    packages=[''],
    url='https://github.com/elias-ramzi/deep-learning-utils',
    license='MIT',
    author='Elias Ramzi',
    author_email='elias.ramzi@lecnam.net',
    description='',
    python_requires='>=3.6',
    install_requires=install_requires
)
