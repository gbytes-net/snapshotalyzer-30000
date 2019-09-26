from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author="Mauricio Roda",
    author_email="rodamauricio@gmail.com",
    description="SnapshotAlyzer 30000 is a tool to mannage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/gbytes-net/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
    
)
