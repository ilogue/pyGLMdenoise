from setuptools import setup, find_packages

requires = []
with open('requirements.txt') as reqfile:
    requires = reqfile.read().splitlines()


setup(
    name='glmdenoise',
    version='0.0',
    description='Python GLMdenoise',
    url='https://github.com/Charestlab/pyGLMdenoise',
    long_description='',
    classifiers=[
      "Programming Language :: Python",
      "Development Status :: 1 - Planning",
      "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
      "Topic :: Scientific/Engineering",
      "Intended Audience :: Science/Research",
      ],
    author='',
    author_email='',
    keywords='neuroscience ',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite="tests",
)
