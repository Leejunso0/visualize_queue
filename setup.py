import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
setuptools.setup(
    name = 'visualize_queue',
    version= '0.0.1.2',
    long_description = long_description,
    long_description_content_type='text/markdown',
    description='visualize queue with matplotlib',
    author = 'junsoo',
    url = 'https://github.com/Leejunso0/visualize_queue',
    download_url= 'https://github.com/Leejunso0/visualize_queue',
    requires=[
        "matplotlib"
    ],
    packages = [ 'visualize_queue' ],
    classifiers= [
        "Programming Language :: Python :: 3"
    ]
)