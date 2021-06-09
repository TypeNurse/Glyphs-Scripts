#MenuTitle: Set Kerning Groups for Composite Glyphs
# -*- coding: utf-8 -*-
__doc__="""
Set kerning groups for selected composite glyphs based on included components.
"""
processedGlyphs = []
selection = Font.selectedLayers

for layer in selection:
	glyph = layer.parent
	if not glyph.leftKerningGroup or not glyph.rightKerningGroup:
		if layer.components:
			firstGlyph = layer.components[0].componentName

			if glyph.subCategory == "Ligature":
				lastGlyph = [c.name for c in layer.components if Font.glyphs[c.name].category != "Mark"][-1]
			else:
				lastGlyph = firstGlyph
			
			leftKerningGroup = ""
			rightKerningGroup = ""
			
			if not glyph.leftKerningGroup:
				leftKerningGroup = Font.glyphs[firstGlyph].leftKerningGroup
				glyph.leftKerningGroup = leftKerningGroup
			if not glyph.rightKerningGroup:
				rightKerningGroup = Font.glyphs[lastGlyph].rightKerningGroup
				glyph.rightKerningGroup = rightKerningGroup

		processedGlyphs.append("\n   %s — %s┃%s" % (glyph.name, leftKerningGroup, rightKerningGroup))
		
if processedGlyphs:
	print("Set kerning groups for:", "".join([g for g in processedGlyphs]))