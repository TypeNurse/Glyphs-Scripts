#MenuTitle: New Tab with Glyphs Using Glyph(s) as Component
# -*- coding: utf-8 -*-
__doc__="""
Open a new tab with all glyphs using selected glyphs as components.
"""

tabText = ''

for layer in Font.selectedLayers:
	componentGlyphName = layer.parent.name
	try: # Glyphs 2/3 compatability
		glyphsUsingComponent = [g.name for g in Font.glyphsContainingComponentWithName_masterId_(componentGlyphName, layer.associatedMasterId)]
	except:
		glyphsUsingComponent = [g.name for g in Font.glyphsContainingComponentWithName_masterID_(componentGlyphName, layer.associatedMasterId)]

	if glyphsUsingComponent:
		tabText += '/%s/%s\n' % (componentGlyphName, "/".join([g for g in glyphsUsingComponent]))

Font.newTab(tabText)