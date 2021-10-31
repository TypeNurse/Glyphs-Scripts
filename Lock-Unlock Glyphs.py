#MenuTitle: Lock/Unlock Glyphs
# -*- coding: utf-8 -*-
__doc__="""
Lock/unlock selected glyphs (same state for entire selection).
"""

selection = Font.selectedLayers

firstLayerLock = not selection[0].parent.locked
selection[0].parent.locked = firstLayerLock

for layer in selection[1:]:
	layer.parent.locked = firstLayerLock

if Font.currentTab:
	Font.currentTab.redraw()
