# Rush 01

## English

A C solver for a 4-by-4 building-visibility puzzle. Digits 1 through 4 represent building heights. Each row and column must contain each height once, and the visible building counts must match the clues outside the grid.

A taller building hides shorter buildings behind it. For example, looking at `2 1 4 3` from the left reveals heights 2 and 4, giving a clue of `2`. The program accepts the 16 outside clues.

### Build and run

```sh
make
make run
./rush-01 '4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2'
```

Pass the 16 space-separated clues as one argument: top four, bottom four, left four, then right four.

An example solution for those clues:

```text
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
```

### Implementation

Uses backtracking to try placements and checks row/column uniqueness and visibility. Prints a solved grid when one exists, or `Error` for invalid or unsatisfiable input.

### Tests

```sh
make test
```

Validates solved grids against row, column, and visibility rules; also checks invalid arguments and unsatisfiable clues.

## 日本語

4×4の「ビルが見える数」のパズルを解くCプログラムです。数字1〜4をビルの高さと考え、各行・列に同じ高さを重複させず、外側から見えるビルの数がヒントと一致する盤面を探します。

手前の高いビルは、その後ろの低いビルを隠します。例えば `2 1 4 3` を左から見ると、高さ2と4の2棟が見えるので、左側のヒントは `2` です。プログラムには盤面の外側16か所のヒントを渡します。

### ビルドと実行

```sh
make
make run
./rush-01 '4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2'
```

16個のヒントを、空白区切りの1つの引数として渡します。順序は上側4個・下側4個・左側4個・右側4個です。

上のヒントに対する解の例です。

```text
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
```

### 実装メモ

バックトラッキングで候補を配置し、行・列の重複と可視数を検査します。解が見つかれば盤面を表示し、不正な引数や解のない入力には `Error` を表示します。

### テスト

```sh
make test
```

解のある盤面を行・列・可視数から検証し、不正な引数と解のないヒントを確認します。
