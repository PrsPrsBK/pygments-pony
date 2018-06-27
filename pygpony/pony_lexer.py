# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, bygroups, default, include, words
from pygments.token import *
import re

class PonyLexer(RegexLexer):
    name = 'Pony'
    aliases = ['pony']
    filenames = ['*.pony']

    tokens = {
        'classname': [
            (r'[A-Z]{1}[a-zA-Z0-9_]\w*', Name.Class, '#pop'),
            default('#pop'),
        ],

        'comment': [
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'.+', Comment.Multiline),
        ],

        'fieldname': [
            (r'[a-zA-Z_\']+', Name.Variable, '#pop'),
            default('#pop'),
        ],

        'funcname': [
            (r'(iso|trn|val|ref|box|tag)(\s+)([a-zA-Z0-9_]+)(?=\()', bygroups(Keyword, Text, Name.Function), '#pop'),
            (r'[a-zA-Z_]+(?=\()', Name.Function, '#pop'),
            default('#pop'),
        ],

        'keywords': [
            (words((
                'as', 'break', 'consume', 'continue', 'do', 'elseif', 'else', 'end',
                'exec', 'finally', 'for', 'in', 'if', 'match',
                'object', 'recover', 'repeat', 'return', 'then', 'try', 'until', 'where', 'while', 'with', 'yield',
                ), suffix=r'\b'),
             Keyword),
            ('error', Error),
            (words((
                'true', 'false'), suffix=r'\b'),
             Keyword.Constant),
            (words((
                '_init', '_final'), suffix=r'\b'),
             Name.Function.Magic),
            # builtin-type
            (words((
                'None',
                'Bool', 'String',
                'ISize', 'ILong', 'I8', 'I16', 'I32', 'I64', 'I128',
                'USize', 'ULong', 'U8', 'U16', 'U32', 'U64', 'U128',
                'F32', 'F64',
                'Env'), suffix=r'\b'),
             Name.Builtin),
        ],

        'simplevalue':[
            include('keywords'),
            (r'0b[01]+[0-1_]*', Number.Bin),
            (r'0x[0-9a-zA-Z]+[0-9a-zA-Z_]*', Number.Hex),
            (r'-?[0-9]+\.[0-9_]+(?:e(?:\+|-)[0-9]+)?', Number.Float),
            (r'-?[0-9]+[0-9_]*', Number.Integer),
            (r"'[^']*'", String.Char),
            (r'"[^"]*"', String.Double),
        ],

        'value': [
            include('whitespace'),
            include('simplevalue'),
        ],

        'whitespace': [
            (r'\s+', Text),
        ],

        'root': [
            # structural part
            (r'//.*$', Comment.Single),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'\(|\)|\[|\]|\{|\}|\||&|,|\.(?!>)|=>|:|;', Punctuation),
            (r'\.>|~|>>|<<|\+|-|\*|%|/|=|==|!=|<=|>=|<|>|!|\^', Operator),
            (r'\b(and|xor|or|not|is|isnt)\b', Operator.Word),
            (r'(actor)(\s+)(Main)', bygroups(Keyword.Declaration, Text, Name.Builtin)),
            (r'(actor|class|primitive|type|trait|interface)(\s+)', bygroups(Keyword.Declaration, Text), 'classname'),
            (r'(var|let|embed)(\s+)', bygroups(Keyword.Declaration, Text), 'fieldname'),
            (r'(fun|be|new)(\s+)', bygroups(Keyword.Declaration, Text), 'funcname'),
            (r'use\b', Keyword.Namespace),

            # non-structural part
            include('value'),
            (r'\b(iso|trn|val|ref|box|tag)\b', Keyword),
            (r'[A-Z]{1}[a-zA-Z0-9_]*\b', Name.Class),
            (r"\bthis(?=\()", Name.Builtin.Pseudo),
            (r"([a-zA-Z0-9_']+)(?=\()", Name.Function),
            (r"[a-zA-Z0-9_']+", Name.Variable),
            (r'.+', Text),
        ],

    }

