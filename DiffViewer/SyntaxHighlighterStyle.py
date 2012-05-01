####################################################################################################
# 
# DiffViewer - Diff Viewer 
# Copyright (C) Salvaire Fabrice 2012 
# 
####################################################################################################

""" This module defines the style for the syntax highlighting. """

####################################################################################################

from PyQt4 import QtGui
from pygments.styles import get_style_by_name

####################################################################################################

class SyntaxHighlighterStyle(dict):

    """ This class defines a QTextCharFormat for each type of tokens defined by Pygments.

    This class has a dictionnary interface.
    """

    ##############################################
    
    def __init__(self, style='default'):

        """ The parameter *style* select the Pygments style. """

        pygments_style = get_style_by_name(style)
        for token, style_attributes in pygments_style.list_styles():
            # style attributes: bgcolor, bold, border, color, italic, mono, roman, sans, underline
            text_format = QtGui.QTextCharFormat()
            def to_brush(colour):
                return QtGui.QColor("#" + colour)
            if style_attributes['bgcolor']:
                text_format.setBackground(to_brush(style_attributes['bgcolor']))
            if style_attributes['color']:
                text_format.setForeground(to_brush(style_attributes['color']))
            if style_attributes['bold']:
                text_format.setFontWeight(QtGui.QFont.Bold)
            if style_attributes['italic']:
                text_format.setFontItalic(True)
            self[token] = text_format

    ##############################################
    
    def __getitem__(self, key):

        """ Return a copy of the QTextCharFormat for the corresponding key. """

        return QtGui.QTextCharFormat(super(SyntaxHighlighterStyle, self).__getitem__(key))
            
####################################################################################################
# 
# End
# 
####################################################################################################
