=============
pygments-pony
=============

**This project is in very early stage. It may works to some extent, but not completely well.**

How to activate
===============

Navigate to pygments-pony directory, and ``pip install -e .`` .
Next, navigate to reST document's directory, do some configs.

* In ``conf.py``, add ``'ponylexer'`` to ``extensions`` array.
* In ``_ext`` directory, make ``ponylexer.py`` file, and write down like following.

.. code-block:: python

    def setup(app):
        try:
            import pygments
            from pygpony.pony_lexer import PonyLexer
        except ImportError:
            pass
        else:
            app.add_lexer('pony', PonyLexer())


After that, specify reST's ``code-block`` as ``pony``, and build the reST documents.

LICENSE
=======

2-Clause BSD

