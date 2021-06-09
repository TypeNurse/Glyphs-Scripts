#MenuTitle: Reverse Selected Text
# -*- coding: utf-8 -*-
__doc__="""
Reverses (LTR ⇄ RTL) all selected text in Edit view.
"""


selection = Font.selectedLayers

if len(selection) >1:
	tab = Font.currentTab   # Set 'tab' to current tab
	
	cursor = tab.textCursor   # Selection starting position
	length = tab.textRange   # Selection length
	lineBreak = GSControlLayer(10)
	
	if lineBreak in selection:
		subStrings = []
		lineBreakIndex = [ i for i, e in enumerate(selection) if e == lineBreak ]
		lines = [ selection[i:j] for i,j in zip([0] + lineBreakIndex, lineBreakIndex + [None]) ]

		for l in lines:
			if lineBreak in l:
				subStrings.append([lineBreak] + l[1:][::-1])
			else:
				subStrings.append(l[::-1])

		reversedSelection = []
		for i in subStrings:
			reversedSelection += i

	else:
		reversedSelection = selection[::-1]
		
	newString = tab.layers[:cursor] + reversedSelection + tab.layers[cursor+length:]

	tab.layers = []
	
	for layer in newString:
		tab.layers.append(layer)
		
else:
	print("Please use the Text tool and select two or more glyphs.")
	Message("Please use the Text tool and select two or more glyphs.", "Reverse Selected Text", OKButton=None)