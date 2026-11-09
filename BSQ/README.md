# BSQ

## English

A C program that finds the largest square containing only empty cells in a rectangular map. It reads a character grid and prints the map with the chosen square filled using another character.

For example, with `.` for empty cells and `o` for obstacles, it finds a square containing no `o`. Ties favor the topmost square, then the leftmost.

### Build and run

Requires a C compiler and Make.

```sh
make
printf '3.ox\n.....\n.....\n.....\n' > map.txt
./bsq map.txt
./bsq < map.txt
```

Pass filenames as arguments, or read standard input with no arguments. Multiple files are supported.

The obstacle-free map above has three rows and five columns, so its leftmost three-by-three area is filled:

```text
xxx..
xxx..
xxx..
```

### Map format

The first line contains the row count followed by the empty, obstacle, and fill characters. In `3.ox`, `3` is the row count, `.` means empty, `o` means obstacle, and `x` fills the chosen square.

Remaining rows must have equal width and end with newlines. Invalid maps produce `map error` on standard error.

### Tests

```sh
make test
```

Checks single cells, rows, columns, all-obstacle maps, ties, invalid maps, standard input, and multiple files.

## 日本語

障害物のある長方形のマップから、空きマスだけでできる最大の正方形を探すCプログラムです。マップを文字で読み込み、見つけた正方形を別の文字で塗った結果を表示します。

例えば `.` が空きマス、`o` が障害物なら、`o` を1つも含まない正方形の領域を探します。同じ大きさが複数ある場合は、上側、次に左側を優先します。

### ビルドと実行

Cコンパイラ・Make が必要です。

```sh
make
printf '3.ox\n.....\n.....\n.....\n' > map.txt
./bsq map.txt
./bsq < map.txt
```

ファイル名を引数に渡すか、引数なしで標準入力から読み込みます。複数のファイル名も指定できます。

上の3行×5列のマップには障害物がないので、左端の3×3マスを塗って表示します。

```text
xxx..
xxx..
xxx..
```

### マップ形式

先頭行は「行数・空きマス・障害物・埋める文字」です。上の例の `3.ox` は3行のマップを表し、空きマスは `.`、障害物は `o`、正方形を埋める文字は `x` です。

残りの各行は同じ幅に揃え、末尾に改行を付けます。不正なマップは `map error` を標準エラー出力に表示します。

### テスト

```sh
make test
```

1マス・1行・1列・全障害物・最大正方形の同順位、不正マップ、標準入力、複数ファイルを確認します。
