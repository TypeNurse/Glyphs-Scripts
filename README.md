# ABOUT
Python scripts for Glyphs font editor. Should be compatible with both version 2 and 3.

## Components and Composites
* **Add Missing Composites for Stylistic Sets:** Add composite glyphs for letters in stylistic sets where the standard glyph is used as component. Useful to maintain consistency in glyph set when adding a new styilistic set.
* **Make Component Smart:** Turn the selected components into smart components based on the axes defined in the font, thus making the interpolatable. Useful for e.g. small caps and ordinals, depending on your setup.
* **New Tab with Glyphs Using Glyph(s) as Component:** Opens a new tab with all glyphs using selected glyphs as components. Same as *”Show all glyphs that uses ...”* in Edit view, but works for multiple glyphs. Each glyphs reports on a separate line of text.
* **Set Kerning Groups for Composite Glyphs:** Sets missing kerning groups for selected composite glyphs based on included components (ignoring marks). Also works for ligatures.

## Glyph Properties
* **Lock/Unlock Glyphs:** Locks or unlocks selected glyphs, resulting in the same lock state for the entire selection. *Recommended shortcut:* ⌘L
* **Toggle Glyph Lock:** Toggles the lock state for selected glyphs. Unlike the above, the lock state if not harmonized across the selection. *Recommended shortcut:* ⌥⌘L
* **Swap Glyph Names:** Exchanges the names of two selected glyphs. All other glyph data remains unchanged.

## Other
* **Remove Annotation:** Deletes all annotation (in all layers) for selected glyphs.
* **Reverse Selected Text:** Reverses (i.e. LTR ⇄ RTL) *selected* text in Edit view. Preserves layers shown and line breaks. Useful in LTR+RTL fonts so you can type test words without have to do it backwards. :)