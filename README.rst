=============
pygments-pony
=============

**This project is in very early stage. Not work.**

How to activate
===============

Navigate to pygments-pony directory, and ``pip install -e .`` .
Next, navigate to reST document's directory, do comfig.

* In ``conf.py``, add ``'ponylexer'`` to ``extensions`` array.
* In ``_ext`` directory, make ``ponylexer.py`` file, and write down like following.

.. code-block:: python

    def setup(app):
        try:
            import pygments
            from pypony.pony_lexer import PonyLexer
        except ImportError:
            pass
        else:
            app.add_lexer('pony', PonyLexer())


After that, specify reST's ``code-block`` as ``pony``, and build the reST documents.

LICENSE
=======

2-Clause BSD

