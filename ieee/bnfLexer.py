# Generated from bnfLexer.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,14,106,6,-1,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,
        7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,
        2,13,7,13,2,14,7,14,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,1,1,1,
        5,1,42,8,1,10,1,12,1,45,9,1,1,2,1,2,5,2,49,8,2,10,2,12,2,52,9,2,
        1,2,1,2,5,2,56,8,2,10,2,12,2,59,9,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,1,11,4,11,89,8,11,11,11,12,11,90,1,12,1,12,1,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,0,0,15,
        2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8,18,9,20,10,22,11,24,12,26,0,
        28,13,30,14,2,0,1,6,1,0,97,122,3,0,48,57,95,95,97,122,1,0,65,90,
        3,0,9,10,13,13,32,32,2,0,91,91,93,93,2,0,39,39,92,92,109,0,2,1,0,
        0,0,0,4,1,0,0,0,0,6,1,0,0,0,0,8,1,0,0,0,0,10,1,0,0,0,0,12,1,0,0,
        0,0,14,1,0,0,0,0,16,1,0,0,0,0,18,1,0,0,0,0,20,1,0,0,0,0,22,1,0,0,
        0,1,24,1,0,0,0,1,26,1,0,0,0,1,28,1,0,0,0,1,30,1,0,0,0,2,32,1,0,0,
        0,4,39,1,0,0,0,6,46,1,0,0,0,8,64,1,0,0,0,10,68,1,0,0,0,12,70,1,0,
        0,0,14,72,1,0,0,0,16,74,1,0,0,0,18,76,1,0,0,0,20,78,1,0,0,0,22,83,
        1,0,0,0,24,88,1,0,0,0,26,92,1,0,0,0,28,97,1,0,0,0,30,102,1,0,0,0,
        32,36,7,0,0,0,33,35,7,1,0,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,
        0,0,0,36,37,1,0,0,0,37,3,1,0,0,0,38,36,1,0,0,0,39,43,7,2,0,0,40,
        42,8,3,0,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,
        0,44,5,1,0,0,0,45,43,1,0,0,0,46,50,5,91,0,0,47,49,8,4,0,0,48,47,
        1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,
        52,50,1,0,0,0,53,57,5,167,0,0,54,56,8,4,0,0,55,54,1,0,0,0,56,59,
        1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,
        60,61,5,93,0,0,61,62,1,0,0,0,62,63,6,2,0,0,63,7,1,0,0,0,64,65,5,
        58,0,0,65,66,5,58,0,0,66,67,5,61,0,0,67,9,1,0,0,0,68,69,5,124,0,
        0,69,11,1,0,0,0,70,71,5,91,0,0,71,13,1,0,0,0,72,73,5,93,0,0,73,15,
        1,0,0,0,74,75,5,123,0,0,75,17,1,0,0,0,76,77,5,125,0,0,77,19,1,0,
        0,0,78,79,5,39,0,0,79,80,1,0,0,0,80,81,6,9,0,0,81,82,6,9,1,0,82,
        21,1,0,0,0,83,84,9,0,0,0,84,85,1,0,0,0,85,86,6,10,0,0,86,23,1,0,
        0,0,87,89,8,5,0,0,88,87,1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,0,90,91,
        1,0,0,0,91,25,1,0,0,0,92,93,5,92,0,0,93,94,7,5,0,0,94,95,1,0,0,0,
        95,96,6,12,2,0,96,27,1,0,0,0,97,98,5,39,0,0,98,99,1,0,0,0,99,100,
        6,13,0,0,100,101,6,13,3,0,101,29,1,0,0,0,102,103,9,0,0,0,103,104,
        1,0,0,0,104,105,6,14,0,0,105,31,1,0,0,0,7,0,1,36,43,50,57,90,4,6,
        0,0,5,1,0,7,12,0,4,0,0
    ]

class bnfLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRING_MODE = 1

    IDENTIFIER = 1
    CAPITALIZED_WORD = 2
    SECTION_REFERENCE = 3
    DOUBLE_COLON_EQUAL = 4
    VERTICAL_BAR = 5
    LEFT_BRACKET = 6
    RIGHT_BRACKET = 7
    LEFT_BRACE = 8
    RIGHT_BRACE = 9
    APOSTROPHE = 10
    OTHER = 11
    STRING_TEXT = 12
    STRING_APOSTROPHE = 13
    STRING_OTHER = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "STRING_MODE" ]

    literalNames = [ "<INVALID>",
            "'::='", "'|'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "CAPITALIZED_WORD", "SECTION_REFERENCE", "DOUBLE_COLON_EQUAL", 
            "VERTICAL_BAR", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
            "RIGHT_BRACE", "APOSTROPHE", "OTHER", "STRING_TEXT", "STRING_APOSTROPHE", 
            "STRING_OTHER" ]

    ruleNames = [ "IDENTIFIER", "CAPITALIZED_WORD", "SECTION_REFERENCE", 
                  "DOUBLE_COLON_EQUAL", "VERTICAL_BAR", "LEFT_BRACKET", 
                  "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", "APOSTROPHE", 
                  "OTHER", "STRING_TEXT", "STRING_ESC_SEQ", "STRING_APOSTROPHE", 
                  "STRING_OTHER" ]

    grammarFileName = "bnfLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


