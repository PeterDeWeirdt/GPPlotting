from setuptools import setup

setup(name='gpplotting',
      version='0.1',
      description='Plotting functions for GPP R&D',
      url='https://github.com/PeterDeWeirdt/GPPlotting',
      author='Peter DeWeirdt, Marissa Feeley, Audrey Griffith, Ruth Hanna, Mudra Hegde, Annabel Sangree, Zsofia Szegletes',
      author_email='pdeweird@broadinstitute.org',
      license='MIT',
      packages=['gpplotting'],
      install_requires =[
            'seaborn',
            'matplotlib',
            'scipy',
            'numpy',
            'pandas',
            'adjustText'
      ],
      zip_safe=False)