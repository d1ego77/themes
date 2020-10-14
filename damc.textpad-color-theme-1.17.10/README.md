
# TextPad (classic and solarized)

These themes were designed to be simple and easy on the eyes

Supported languages: Rust, Go, Python, Ruby, Java, Javascript, C#, C, C++, Typescript, PHP, Elixir, Groovy, Lua, html, Clojure and more ...

## TextPad Classic
<p align="center">
<img  src="https://raw.githubusercontent.com/damc-code/themes/master/damc.textpad-color.images.examples/textpadclassic3.png"  title="TextPad Classic" />
</p>

## TextPad Solarized Dark
<p align="center">
<img  src="https://raw.githubusercontent.com/damc-code/themes/master/damc.textpad-color.images.examples/textpadsolarizeddark3.png"  title="TextPad Solarized Dark" />
</p>

## TextPad Solarized light
<p align="center">
<img  src="https://raw.githubusercontent.com/damc-code/themes/master/damc.textpad-color.images.examples/textpadsolarizedlight3.png"  title="TextPad Solarized light" />
</p>

## TextPad Classic Solarized
<p align="center">
<img  src="https://raw.githubusercontent.com/damc-code/themes/master/damc.textpad-color.images.examples/textpadclassicsolarized3.png"  title="TextPad Classic Solarized" />
</p>
Do you want your editor looks like the previous images?
Follow these steps:

1. Disable the VSCode Explorer options "Open editors", "Outline", "NPM Scripts"

2. Install [Bracket Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2), [Cascadia Font](https://github.com/microsoft/cascadia-code/releases) and [TextPad icon theme](https://marketplace.visualstudio.com/items?itemName=damc.textpad-icon-theme). 

3. Use these settings:

```js

{
"editor.fontFamily": "Iosevka",
"editor.fontLigatures": true,
"editor.fontSize": 13,
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

4. For TextPad solarized dark and light use this bracket color

``` js
"bracket-pair-colorizer-2.colors": [
"#FC0D1B",
"#FC0D1B",
"#FC0D1B",
],
```

5. For Textpad Classic and Classic Solarized use this bracket color

``` js
"bracket-pair-colorizer-2.colors": [
"#d33682",
"#d33682",
"#d33682",
],
```