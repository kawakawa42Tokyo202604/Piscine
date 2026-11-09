# Piscine C 09

## English

C exercises that package custom functions into a reusable static library, `libft.a`. A library contains compiled functions to link into an executable.

Shell scripts and Makefiles build functions for displaying, comparing, and measuring strings. The supplied demo calls functions from the resulting library.

### Exercises

| Location | Source | Behavior |
| --- | --- | --- |
| ex00 | [Sources and build script](ex00/) | Build a library of basic functions using a Shell script |
| ex01 | [Makefile](ex01/Makefile) to build `libft.a` | Rebuild required files with Make |

### Build and run

Requires a C compiler and Make, ar, and ranlib.

```sh
make
make run
```

Builds `ex01/libft.a` and `build/example` using the supplied [main.c](main.c). For the Shell version, enter `ex00` and run `sh libft_creator.sh`.

`make run` calls the library output function and prints `Hello, 42!`.

## 日本語

自作したC関数を、他のプログラムで再利用できる静的ライブラリ `libft.a` にまとめる演習です。ライブラリは複数の関数のコンパイル結果をまとめたファイルで、実行プログラムを作るときに組み込みます。

文字列の表示・比較・文字数の取得などを、ShellスクリプトまたはMakefileからビルドします。付属の実行例で、ライブラリの関数を呼び出すところまで確認できます。

### 演習

| 場所 | ソース | 処理 |
| --- | --- | --- |
| ex00 | [ソースとビルドスクリプト](ex00/) | 基本関数をShellスクリプトでライブラリ化 |
| ex01 | [Makefile](ex01/Makefile) による `libft.a` の生成 | Makefileで必要なファイルだけを再ビルド |

### ビルドと実行

Cコンパイラ・Make・ar・ranlib が必要です。

```sh
make
make run
```

`ex01/libft.a` と、付属の [main.c](main.c) を使う `build/example` を生成します。`ex00` のシェルスクリプト版は、そのディレクトリで `sh libft_creator.sh` を実行します。

`make run` は、ライブラリにまとめた表示関数を呼び出し、`Hello, 42!` を表示します。
