# Piscine C 05

## English

C exercises for factorials, powers, Fibonacci numbers, and prime checks. They use both loops and recursion, where a function calls itself.

The final exercise finds placements of ten queens on a ten-by-ten board so that none can attack another.

### Exercises

| Location | Source | Behavior |
| --- | --- | --- |
| ex00 | [ft_iterative_factorial.c](ex00/ft_iterative_factorial.c) | Iterative factorial |
| ex01 | [ft_recursive_factorial.c](ex01/ft_recursive_factorial.c) | Recursive factorial |
| ex02 | [ft_iterative_power.c](ex02/ft_iterative_power.c) | Iterative power |
| ex03 | [ft_recursive_power.c](ex03/ft_recursive_power.c) | Recursive power |
| ex04 | [ft_fibonacci.c](ex04/ft_fibonacci.c) | Fibonacci number |
| ex05 | [ft_sqrt.c](ex05/ft_sqrt.c) | Integer square root |
| ex06 | [ft_is_prime.c](ex06/ft_is_prime.c) | Primality test |
| ex07 | [ft_find_next_prime.c](ex07/ft_find_next_prime.c) | First prime at or above the input |
| ex08 | [ft_ten_queens_puzzle.c](ex08/ft_ten_queens_puzzle.c) | Enumerate ten-queens placements |

### Build and run

Requires a C compiler and Make.

```sh
make
make run EX=ex00
```

Combines the supplied [main.c](main.c) with each exercise to create executables such as `build/ex00`. Select an exercise with `EX` and pass runtime arguments through `ARGS`.

`ex00` prints `120`, the factorial of 5: 5 x 4 x 3 x 2 x 1.

## 日本語

階乗・累乗・フィボナッチ数・素数判定などを計算するC演習です。繰り返しで計算する方法と、関数が自分自身を呼ぶ再帰で計算する方法を扱います。

最後の演習では、10×10の盤に10個のクイーンを互いに攻撃できない位置へ置く組み合わせを探します。

### 演習

| 場所 | ソース | 処理 |
| --- | --- | --- |
| ex00 | [ft_iterative_factorial.c](ex00/ft_iterative_factorial.c) | 繰り返しで階乗を計算 |
| ex01 | [ft_recursive_factorial.c](ex01/ft_recursive_factorial.c) | 再帰で階乗を計算 |
| ex02 | [ft_iterative_power.c](ex02/ft_iterative_power.c) | 繰り返しで累乗を計算 |
| ex03 | [ft_recursive_power.c](ex03/ft_recursive_power.c) | 再帰で累乗を計算 |
| ex04 | [ft_fibonacci.c](ex04/ft_fibonacci.c) | フィボナッチ数を求める |
| ex05 | [ft_sqrt.c](ex05/ft_sqrt.c) | 整数になる平方根を求める |
| ex06 | [ft_is_prime.c](ex06/ft_is_prime.c) | 素数かどうかを判定 |
| ex07 | [ft_find_next_prime.c](ex07/ft_find_next_prime.c) | 指定値以上で最初の素数を探す |
| ex08 | [ft_ten_queens_puzzle.c](ex08/ft_ten_queens_puzzle.c) | 10個のクイーンの配置を列挙 |

### ビルドと実行

Cコンパイラ・Make が必要です。

```sh
make
make run EX=ex00
```

付属の [main.c](main.c) と各演習のソースを組み合わせ、`build/ex00` などの実行ファイルを生成します。 `EX` で演習を選び、`ARGS` で実行時の引数を渡せます。

`ex00` の実行例は、5の階乗（5×4×3×2×1）である `120` を表示します。
