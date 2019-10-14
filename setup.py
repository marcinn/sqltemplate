from setuptools import setup, find_packages

setup(name='sqltemplate',
      version='0.5.4',
      description='Core library for database querying tools '
                  'based on templates',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        ],
      author='Marcin Nowak',
      author_email='marcin.j.nowak@gmail.com',
      url='https://github.com/marcinn/sqltemplate',
      install_requires=['flatdict>=1.2.0,<2.0.0', 'six'],
      extras_require={
          'prettysql': 'sqlparse>=0.1.19,<1.0',
          },
      keywords='python sql template',
      packages=find_packages('.'),
      include_package_data=True,
      test_suite='nose.collector',
      zip_safe=True,
      )
