from setuptools import setup, find_packages

README = 'create IPython consoles with custom banners'

requires = [ 'ipython==8.10.0' ]

setup(name='myconsole',
      version='1.0.2',
      description=README,
      long_description=README,
      url='https://github.com/haarcuba/myconsole',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Yoav Kleinberger',
      author_email='haarcuba@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      [console_scripts]
      myconsole-demo = myconsole.demo:main
      """,
      )
