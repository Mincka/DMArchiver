from setuptools import setup, find_packages
 
import dmarchiver

setup(
 
    name='dmarchiver',
    version=dmarchiver.__version__,
 
    packages=find_packages(),

    install_requires=['requests==2.11.1', 'lxml==3.6.4', 'cssselect==0.9.2'],    

    author="Julien EHRHART",
    author_email="julien.ehrhart@live.com",
 
    description="A tool to archive the direct messages from your private conversations on Twitter.",
 
    long_description=open('README.md').read(),
 
    include_package_data=True,
 
    url='https://github.com/Mincka/DMArchiver',
 
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Topic :: System :: Archiving",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
 
    entry_points = {
        'console_scripts': [
            'dmarchiver = dmarchiver.cmdline:main',
        ],
    },
 
    license="GNU General Public License v3 (GPLv3)",
)
