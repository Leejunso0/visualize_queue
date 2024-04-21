import setuptools

setuptools.setup(
    name = 'visualize_queue',
    version= '0.0.1',
    description='visualize queue with matplotlib',
    author = 'junsoo',
    url = 'https://github.com/Leejunso0/visualize_queue',
    download_url= 'https://github.com/Leejunso0/visualize_queue',
    requires=[
        "matplotlib==3.8.4"
    ],
    packages = [ 'visualize_queue' ],
    classifiers= [
        "Programming Language :: Python :: 3"
    ]
)