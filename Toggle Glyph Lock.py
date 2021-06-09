#MenuTitle: Toggle Glyph Lock
# -*- coding: utf-8 -*-
__doc__="""
Toggle the lock state for selected glyphs.
"""

for layer in Font.selectedLayers:
	layer.parent.locked = not layer.parent.locked