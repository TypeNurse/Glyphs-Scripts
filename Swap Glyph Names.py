#MenuTitle: Swap Glyph Names
# -*- coding: utf-8 -*-
__doc__="""
Exchange names for two selected glyphs.
"""

selection = Font.selectedLayers

if len(selection) == 2:
	glyphNames = [l.parent.name for l in selection]
	selection[1].parent.name = 'swapGlyphNamesTemp'

	selection[0].parent.name = glyphNames[1]
	selection[1].parent.name = glyphNames[0]
	
	print('%s ⇄ %s' % (glyphNames[0], glyphNames[1]))

else:
	Message('Select exacly TWO glyphs.', title='Swap Glyph Names', OKButton=None)