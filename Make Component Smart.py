#MenuTitle: Make Component Smart
# -*- coding: utf-8 -*-
__doc__="""
Turn the selected components into smart components, based on the axes defined in the font.
"""

selectedLayer = Font.selectedLayers[0]
processedGlyphs = []

for component in selectedLayer.components:
	if component.selected:
		componentGlyph = Font.glyphs[component.name]

		# Check if component is already smart
		if not componentGlyph.smartComponentAxes:
			for i in range(len(Font.axes)):
				axisValues = [m.axes[i] for m in Font.masters]
				newAxis = GSSmartComponentAxis()
				newAxis.name = Font.axes[i].name
				newAxis.bottomValue = min(axisValues)
				newAxis.topValue = max(axisValues)
				componentGlyph.smartComponentAxes.append(newAxis)
				
				for layer in componentGlyph.layers:
					if layer.isMasterLayer:
						if Font.masters[layer.associatedMasterId].axes[i] == newAxis.bottomValue:
							layer.smartComponentPoleMapping[componentGlyph.smartComponentAxes[newAxis.name].id] = 1
						if Font.masters[layer.associatedMasterId].axes[i] == newAxis.topValue:
							layer.smartComponentPoleMapping[componentGlyph.smartComponentAxes[newAxis.name].id] = 2
				
				processedGlyphs.append(componentGlyph.name)
		
		# Renew selection in order to show smart glyph controls
		component.selected = False
		component.selected = True
		
print('%s are now smart glyphs.' % ", ".join(processedGlyphs))