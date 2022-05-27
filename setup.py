from distutils.core import setup

setup(
    name = 'animedev',
    packages = ['animedev'],
    version = '1.0.0',
    license = 'Apache-2.0',
    description = 'A 9anime.dev scrapper module for python.', 
    author = 'Sasta Dev',
    author_email = 'sastadev2007@gmail.com',
    url = 'https://github.com/SastaDev/9AnimeDev',
    download_url = 'https://github.com/SastaDev/9AnimeDev/archive/refs/tags/v0.0.1.tar.gz',
    keywords = ['9animedev', 'animedev'],
    install_requires = [
        'requests'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)