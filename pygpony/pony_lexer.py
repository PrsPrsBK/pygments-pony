# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, bygroups, default, include, words
from pygments.token import *
import re

class PonyLexer(RegexLexer):
    name = 'Pony'
    aliases = ['pony']
    filenames = ['*.pony']

    tokens = {
        'classDecl': [
            (r'[A-Z]{1}[a-zA-Z0-9_]\w*', Name.Class, '#pop'),
            default('#pop'),
        ],

        'comment': [
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'.+', Comment.Multiline),
        ],

        'fieldDecl': [
            (r'[a-zA-Z_\']+', Name.Variable, '#pop'),
            default('#pop'),
        ],

        'funcDecl': [
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
                'None', 'Any', 'Env', 'AmbientAuth', 'Pointer', 'MaybePointer',
                'Bool', 'String', 'Stringable', 'StringBytes', 'StringRunes',
                'ISize', 'ILong', 'I8', 'I16', 'I32', 'I64', 'I128', 'Signed',
                'USize', 'ULong', 'U8', 'U16', 'U32', 'U64', 'U128', 'Unsigned', 'Integer', 'Int',
                'F32', 'F64', 'Real', 'FloatingPoint', 'Float', 'Number',
                'Array', 'ArrayKeys', 'ArrayValues', 'ArrayPairs',
                'Seq', 'ByteSeq', 'ByteSeqIter',
                'ReadSeq', 'ReadElement', 'Iterator',
                'Stdin', 'StdStream', 'InputNotify', 'InputStream', 'OutStream',
                'Less', 'Equal', 'Greater', 'Compare', 'HasEq', 'Equatable', 'Comparable',
                'AsioEventID', 'AsioEventNotify', 'AsioEvent',
                'DisposableActor', 'SourceLoc', 'DoNotOptimize', 'Platform',
                '_UTF32Encoder', '_SignedCheckedArithmetic', '_ArithmeticConvertible',
                '_SignedInteger', '_UnsignedInteger', '_ToString',
                ), suffix=r'\b'),
             Name.Builtin),
        ],

        'simplevalue':[
            include('keywords'),
            (r'0b[01]+[0-1_]*', Number.Bin),
            (r'0x[0-9a-zA-Z]+[0-9a-zA-Z_]*', Number.Hex),
            (r'-?[0-9]+\.[0-9_]+(?:e(?:\+|-)[0-9]+)?', Number.Float),
            (r'-?[0-9]+[0-9_]*', Number.Integer),
            (r"'[^']*'", String.Char),
            # (r'"[^"]*"', String.Double),
            (r'"', String.Double, 'stringSeq'), # if buggy, discard this line and recover simple one.
        ],

        'stringSeq': [
            (r'\\([\\abefnrtv"\'0]|[uU]{1}[a-fA-F0-9]{6}|[uU]{1}[a-fA-F0-9]{4}|x[a-fA-F0-9]{2})', String.Escape),
            (r'"', String.Double, '#pop'),
            (r'[^"\\]+', String.Double),
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
            (r'\(|\)|\[|\]|\{|\}|,|\.(?!>)|=>|:|;', Punctuation),
            (r'\.>|~|>>|<<|\||&|\+|-|\*|%|/|=|==|!=|<=|>=|<|>|!|\^', Operator),
            (r'\b(and|xor|or|not|is|isnt)\b', Operator.Word),
            (r'(actor)(\s+)(Main)', bygroups(Keyword.Declaration, Text, Name.Builtin)),
            (r'(actor|class|primitive|type|trait|interface)(\s+)', bygroups(Keyword.Declaration, Text), 'classDecl'),
            (r'(var|let|embed)(\s+)', bygroups(Keyword.Declaration, Text), 'fieldDecl'),
            (r'(fun|be|new)(\s+)', bygroups(Keyword.Declaration, Text), 'funcDecl'),
            (r'use\b', Keyword.Namespace),

            # non-structural part
            include('value'),
            (r'\?', Text),
            (r'\b(iso|trn|val|ref|box|tag)\b', Keyword),
            (r'_?[A-Z]{1}[a-zA-Z0-9_]*\b', Name.Class),
            (r"\bthis(?=\()", Name.Builtin.Pseudo),
            (r"([a-zA-Z0-9_']+)(?=\()", Name.Function),
            (r"[a-zA-Z0-9_']+", Name.Variable),
            (r'.+', Text),
        ],

    }

