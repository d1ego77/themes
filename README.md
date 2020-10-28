
# TextPad

This theme was designed to be simple, it is based on color scheme of the old Textpad editor

## Syntax Palette

| Scope       | Color                                              | Scope   | RGB                |
| ------------| -------------------------------------------------- | ------- | ------------------ |
| Background | ![#F7F7F7](https://placehold.it/35/F7F7F7/?text=+) | Foreground | ![#000000](https://placehold.it/35/000000/?text=+) |
| Comments | ![#008000](https://placehold.it/35/008000/?text=+) | Keywords/Primitives | ![#1100FF](https://placehold.it/35/1100FF/?text=+) |
| Brackets | ![#DC322F](https://placehold.it/35/DC322F/?text=+) | Strings | ![#008080](https://placehold.it/35/008080/?text=+) |
| Storage/Support | ![#0000AA](https://placehold.it/35/0000AA/?text=+) | Constants | ![#AD4011](https://placehold.it/35/AD4011/?text=+) |


<!-- | Background           | ![#F7F7F7](https://placehold.it/25/F7F7F7/?text=+) | #F7F7F7 |Foreground           | ![#000000](https://placehold.it/25/000000/?text=+) | #000000 |
| Comments             | ![#008000](https://placehold.it/25/008000/?text=+) | #008000 |Keywords/Primitives  | ![#1100FF](https://placehold.it/25/1100FF/?text=+) | #1100FF |
| Brackets             | ![#DC322F](https://placehold.it/25/DC322F/?text=+) | #DC322F | Strings | `![#008080](https://placehold.it/25/008080/?text=+) | #008080 | 
| Storage-Support      | ![#0000AA](https://placehold.it/25/0000AA/?text=+) | #0000AA | Constants            | ![#AD4011](https://placehold.it/25/AD4011/?text=+) | #AD4011 | -->

## Preview
<p align="center">
<img  src="https://raw.githubusercontent.com/damc-code/themes/master/damc.textpad-color.images.examples/textpad.png"  title="TextPad" />
</p>
Tested languages: Rust, Go, Python, Ruby, Java, Javascript, C#, C, C++, Typescript, PHP, Elixir, Groovy, Lua, Clojure, HTML

Do you want your editor looks like the previous image?
Follow these steps:

1. Disable the VSCode explorer options "Open editors", "Outline", "NPM Scripts"

2. Install [Bracket Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2), [PT Mono](https://fonts.google.com/specimen/PT+Mono#standard-styles) font, and [TextPad icon theme](https://marketplace.visualstudio.com/items?itemName=damc.textpad-icon-theme)(Minimal Black (Chalice Edition)). 

3. Use these settings:

```js

{
"editor.fontFamily": "PT Mono, Cascadia Code,'Courier New'",
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
"workbench.tree.indent": 10,
"editor.renderWhitespace": "none",
"editor.occurrencesHighlight": false,
"editor.selectionHighlight": false,
"bracket-pair-colorizer-2.colors": [
    "#DC322F",
    "#DC322F",
    "#DC322F",
],
"bracket-pair-colorizer-2.showBracketsInGutter": false,
"bracket-pair-colorizer-2.showVerticalScopeLine": false,
"bracket-pair-colorizer-2.highlightActiveScope": false,
"bracket-pair-colorizer-2.showHorizontalScopeLine": false,
}

```