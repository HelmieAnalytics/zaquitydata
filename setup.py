from setuptools import find_packages, setup

setup(
    name='xardata',
    
    packages=find_packages(include=['xardata']),
    
    version='0.1.0',
    
    description='A stock price data import package',
    
    author='HelmieAnalytics',

    url='https://github.com/HelmieAnalytics/xardata',
    
    long_description= open('README.md').read(),#+ '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",

    install_requires= ['yfinance','yahooquery==2.3.7'],

    setup_requires= ['pytest-runner'],

    tests_require= ['pytest==4.4.1'],

    test_suite= 'tests',

    keywords= ['Data Mining', 'Data Science', 'Equities', 'Stocks'],
)
