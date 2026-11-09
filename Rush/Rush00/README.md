# Rush 00

## English

A C program that draws a rectangle in the terminal using characters. Five drawing functions use different characters for corners and edges.

For example, `rush(5, 3)` draws a frame five characters wide and three lines tall. Set the size in `main.c` and choose a pattern at build time.

### Build and run

```sh
make
make run
make run PATTERN=01
```

The size is set by the call `rush(x, y)` in `main.c`, currently `rush(1, 2)`.

### Patterns

`rush00.c` through `rush04.c` use different corner and edge characters. Select `00` through `04` with `PATTERN`, such as `make run PATTERN=04`.

### Output example

With `rush00.c` and a call to `rush(5, 3)`, the output is:

```text
o---o
|   |
o---o
```

### Tests

```sh
make test
```

Checks all five patterns at normal sizes, one cell, one row, one column, and with zero or negative dimensions.

## 日本語

指定した幅と高さの長方形を、文字だけで端末に描くCプログラムです。角・横辺・縦辺に使う文字が異なる5種類の描画関数があります。

例えば `rush(5, 3)` は幅5文字・高さ3行の枠を描きます。サイズは呼び出し用の `main.c` で決め、ビルド時に描画パターンを選びます。

### ビルドと実行

```sh
make
make run
make run PATTERN=01
```

サイズは `main.c` の `rush(x, y)` で指定します。現在の呼び出しは `rush(1, 2)` です。

### パターン

`rush00.c` 〜 `rush04.c` が、それぞれ異なる角・辺の文字を使います。`make run PATTERN=04` のように、`PATTERN` に `00`〜`04` を指定して選べます。

### 出力例

`rush00.c` を選び、`main.c` を `rush(5, 3)` にした場合は次の枠を表示します。

```text
o---o
|   |
o---o
```

### テスト

```sh
make test
```

5パターンの通常サイズ、1マス・1行・1列、幅や高さが0・負の場合を確認します。
