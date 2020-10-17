
# TextPad

This theme was designed to be simple, it is based on color scheme of the old Textpad editor

Tested languages: Rust, Go, Python, Ruby, Java, Javascript (React, NodeJS), C#, C, C++, Typescript (Angular), PHP, Elixir, Groovy, Lua, HTML, Clojure 

## Preview
<p align="center">
<img  src="https://raw.githubusercontent.com/damc-code/themes/master/damc.textpad-color.images.examples/textpad.png"  title="TextPad" />
</p>


Do you want your editor looks like the previous image?
Follow these steps:

1. Disable the VSCode explorer options "Open editors", "Outline", "NPM Scripts"

2. Install [Bracket Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2), [PT Mono](https://fonts.google.com/specimen/PT+Mono#standard-styles), and [TextPad icon theme](https://marketplace.visualstudio.com/items?itemName=damc.textpad-icon-theme). 

3. Use these settings:

```js

{
"editor.fontFamily": "Cascadia Code,'Courier New'",
"editor.fontLigatures": true,
"editor.fontSize": 12,
"breadcrumbs.enabled": false,
"editor.cursorSmoothCaretAnimation": false,
"editor.minimap.enabled": false,
"editor.smoothScrolling": true,
"explorer.decorations.colors": false,
"editor.renderIndentGuides": true,
"workbench.editor.showIcons": false,
"workbench.editor.tabCloseButton": "left",
"editor.renderWhitespace": "none",
"workbench.statusBar.visible": false,
"workbench.activityBar.visible": true,
"editor.occurrencesHighlight": false,
"editor.selectionHighlight": false,
"bracket-pair-colorizer-2.colors": [
    "#FC0D1B",
    "#FC0D1B",
    "#FC0D1B",
],
"bracket-pair-colorizer-2.showBracketsInGutter": false,
"bracket-pair-colorizer-2.showVerticalScopeLine": false,
"bracket-pair-colorizer-2.highlightActiveScope": false,
"bracket-pair-colorizer-2.showHorizontalScopeLine": false,
}

```
