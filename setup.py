from setuptools import setup

setup(name='python-grpc-boilerplate',
      python_requires='>=3.8',
      author='Anthony Corletti',
      author_email='anthcor@gmail.com',
      url='https://github.com/anthcor/python-grpc-boilerplate',
      license='MIT License',
      zip_safe=True,
      install_requires=[
          "grpcio-tools==1.32.0",
          "grpcio==1.32.0",
      ])
