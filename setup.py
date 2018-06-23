from setuptools import setup, find_packages
setup(
    name = "pygments-pony",
    version = "0.1",
    packages = ['pygpony',],
    install_requires = ['Pygments'],
    author = "PrsPrsBK",
    author_email = "prsprsbk@gmail.com",
    description = "Pygments Pony formatter",

    entry_points={
        'pygments.lexers': ['release = pygpony.pony_lexer:PonyLexer', ]
    },

)