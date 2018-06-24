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
            (r'[^*/]', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline),
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
                'break', 'continue', 'del', 'elif', 'else', 'end',
                'exec', 'finally', 'for', 'in', 'if', 'match',
                'object', 'recover', 'ref', 'repeat', 'return', 'try', 'use', 'while', 'yield',
                'as', 'with'), suffix=r'\b'),
             Keyword),
            (words((
                'true', 'false', 'None'), suffix=r'\b'),
             Keyword.Constant),
        ],

        'simplevalue':[
            include('keywords'),
            (r'-?[0-9_]+', Number.Integer),
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
            include('value'),
            (r'//.*$', Comment.Single),
            (r'\(|\)|\[|\]|\{|\}|=>', Punctuation),
            (r'(iso|trn|val|ref|box|tag)\^?', Keyword),
            (r'[A-Z]{1}[a-zA-Z0-9_]*\b', Name.Class),
            (r'[a-zA-Z0-9_]+\b', Name.Variable),
            (r'(class|actor|primitive|type)((?:\s)+)', bygroups(Keyword.Declaration, Text), 'classname'),
            (r'(var|let|embed)((?:\s)+)', bygroups(Keyword.Declaration, Text), 'fieldname'),
            (r'(fun|be|new)((?:\s)+)', bygroups(Keyword.Declaration, Text), 'funcname'),
            (r'(\s*:\s*)', bygroups(Text), 'classname'),
            (r'\+|-|\*|/|=|==|!=|<=|>=|<|>', Operator),
            (r'(is|isnt)\b', Operator.Word),
            (r'/\*', Comment.Multiline, '#push'),
            (r'.+', Text),
        ],

    }

