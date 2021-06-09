#MenuTitle: Remove Annotation
# -*- coding: utf-8 -*-
__doc__="""
Delete all annotation for selected glyphs (in all layers).
"""

processedGlyphs = []

for layer in Font.selectedLayers:
	g = layer.parent
	for l in g.layers:
		if l.annotations:
			l.setAnnotations_(None)
			if g.name not in processedGlyphs:
				processedGlyphs.append(g.name)

if not processedGlyphs:
	print('No annotation to delete.')
else:
	print('Deleted all annotation in glyphs:')
	print('   %s' % ", ".join(processedGlyphs))