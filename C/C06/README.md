# Piscine C 06

## English

C programs that accept, display, and sort strings supplied at startup. The executable name and additional arguments are accessed as arrays.

For example, the sorting program takes `banana apple cherry` and prints `apple`, `banana`, and `cherry`, one per line.

### Exercises

| Location | Source | Behavior |
| --- | --- | --- |
| ex00 | [ft_print_program_name.c](ex00/ft_print_program_name.c) | Print the executable name |
| ex01 | [ft_print_params.c](ex01/ft_print_params.c) | Print arguments in order |
| ex02 | [ft_rev_params.c](ex02/ft_rev_params.c) | Print arguments in reverse input order |
| ex03 | [ft_sort_params.c](ex03/ft_sort_params.c) | Print arguments in lexical order |

### Build and run

Requires a C compiler and Make.

```sh
make
make run EX=ex03 ARGS="banana apple cherry"
```

Builds `build/ex00` through `build/ex03` using the `main` functions already present in each source. Select an exercise with `EX` and pass runtime arguments through `ARGS`.

The example prints `apple`, `banana`, and `cherry`, one per line.

## 日本語

プログラムを起動するときに渡した文字列を受け取り、表示・並べ替えするC演習です。実行ファイル名や追加の引数を、配列として扱います。

例えば並べ替えのプログラムに `banana apple cherry` を渡すと、`apple`・`banana`・`cherry` の順で1行ずつ表示します。

### 演習

| 場所 | ソース | 処理 |
| --- | --- | --- |
| ex00 | [ft_print_program_name.c](ex00/ft_print_program_name.c) | 起動時の実行ファイル名を表示 |
| ex01 | [ft_print_params.c](ex01/ft_print_params.c) | 引数を順に表示 |
| ex02 | [ft_rev_params.c](ex02/ft_rev_params.c) | 引数を渡された順序と逆に表示 |
| ex03 | [ft_sort_params.c](ex03/ft_sort_params.c) | 引数を辞書順に表示 |

### ビルドと実行

Cコンパイラ・Make が必要です。

```sh
make
make run EX=ex03 ARGS="banana apple cherry"
```

各ソースにある既存の `main` を使い、`build/ex00` 〜 `build/ex03` を生成します。 `EX` で演習を選び、`ARGS` で実行時の引数を渡せます。

上の並べ替え例は、`apple`・`banana`・`cherry` を1行ずつ表示します。
