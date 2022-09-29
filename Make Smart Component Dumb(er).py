#MenuTitle: Make Smart Component Dumb(er)
# -*- coding: utf-8 -*-
__doc__="""
Turn the selected smart components into regular components.
"""

selectedLayer = Font.selectedLayers[0]
processedGlyphs = []

for component in selectedLayer.components:
	# Check if component is smart and selected
	if component.selected and component.component.smartComponentAxes:
		componentGlyph = component.component

		for i in range(len(componentGlyph.smartComponentAxes)):
			del componentGlyph.smartComponentAxes[i]
		
		processedGlyphs.append(componentGlyph.name)
		
		# Renew selection in order to hide smart glyph controls
		component.selected = False
		component.selected = True
		
if processedGlyphs:
	be = "are" if len(processedGlyphs)>1 else "is"
	print('%s %s no longer smart.' % (", ".join(processedGlyphs), be))