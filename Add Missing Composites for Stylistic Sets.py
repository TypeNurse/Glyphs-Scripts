#MenuTitle: Add Missing Composites for Stylistic Sets
# -*- coding: utf-8 -*-
__doc__="""
Add composite glyphs for letters in stylistic sets where the standard glyph is used as component.
"""

allLetters = [g.name for g in Font.glyphs if g.category == 'Letter']
tabText = ''

# Make list of tuples with pairs of glyphs with .ss
glyphPairsWithStylisticSet = []
for g in allLetters:
	if ".ss" in g:
		glyphPairsWithStylisticSet.append((g[:g.index('.ss')], g[g.index('.ss'):]))

lettersWithStylisticSets = {}
for k, v in glyphPairsWithStylisticSet:
	lettersWithStylisticSets.setdefault(k, []).append(v)

for key in lettersWithStylisticSets:
	try: # Glyphs 2/3 compatability
		compositeGlyphs = Font.glyphsContainingComponentWithName_masterId_(key, Font.masters[0].id)
	except:
		compositeGlyphs = Font.glyphsContainingComponentWithName_masterID_(key, Font.masters[0].id)
	if compositeGlyphs:
		compositeLetters = [g for g in compositeGlyphs if g.name in allLetters]
		for stylisticSet in lettersWithStylisticSets[key]:
			for compositeLetter in compositeLetters:
				if len(compositeLetter.layers[0].components) > 1:
					newGlyph = compositeLetter.name + stylisticSet
					if newGlyph not in Font.glyphs:				
						Font.glyphs.append(GSGlyph(newGlyph))
#						Font.glyphs[newGlyph].color = 6
						for layer in Font.glyphs[newGlyph].layers:
							layer.makeComponents()
						tabText += '/%s' % newGlyph
				else:
					continue
					
Font.newTab(tabText)