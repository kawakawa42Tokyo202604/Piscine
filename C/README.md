# Piscine C

## English

Exercises in writing small C functions and programs. They progress from printing characters to processing strings, calculating integers, allocating arrays, and creating a library.

`C00` through `C09` are topics; `ex00`, `ex01`, and similar directories are individual exercises. For example, C01's `ft_swap` exchanges integers, and C03's `ft_strstr` searches a string for a substring.

### Topics

| Topic | Contents |
| --- | --- |
| [C 00](C00/README.md) | Character and number output, loops |
| [C 01](C01/README.md) | Updating values through pointers, arrays |
| [C 02](C02/README.md) | String copying, character checks, and letter case |
| [C 03](C03/README.md) | String comparison, joining, and search |
| [C 04](C04/README.md) | Integer parsing and number-base conversion |
| [C 05](C05/README.md) | Recursion, sequences, primes, and queens |
| [C 06](C06/README.md) | Displaying and sorting command-line arguments |
| [C 07](C07/README.md) | Dynamic allocation, ranges, string joining and splitting |
| [C 08](C08/README.md) | Headers, macros, and structures |
| [C 09](C09/README.md) | Static libraries and build automation |

### Usage

Function-only sources need a `main` entry point that calls them. C01, C03 through C06, and C09 include Makefiles and demonstrations. C00, C02, C07, and C08 contain unfinished exercises.

```sh
cd C06
make
make run EX=ex03 ARGS="banana apple cherry"
```

## 日本語

C言語の小さな関数やプログラムを自作する演習集です。文字の表示から始まり、文字列の加工、整数の計算、配列の作成、関数をまとめたライブラリの生成へ進みます。

`C00`〜`C09` がテーマ、各 `ex00`・`ex01` などが個別の演習です。C01の `ft_swap` は2つの整数を交換し、C03の `ft_strstr` は文字列の中から指定した文字列を探します。

### 演習

| 課題 | 内容 |
| --- | --- |
| [C 00](C00/README.md) | 文字や数値の出力とループ |
| [C 01](C01/README.md) | ポインタを通した値の変更と配列操作 |
| [C 02](C02/README.md) | 文字列のコピー・文字種の判定・大文字小文字の変換 |
| [C 03](C03/README.md) | 文字列の比較・連結・検索 |
| [C 04](C04/README.md) | 文字列と整数の変換・基数変換 |
| [C 05](C05/README.md) | 再帰・数列・素数・クイーン配置 |
| [C 06](C06/README.md) | コマンドライン引数の表示と並べ替え |
| [C 07](C07/README.md) | 動的メモリ確保・配列生成・文字列の結合と分割 |
| [C 08](C08/README.md) | ヘッダー・マクロ・構造体 |
| [C 09](C09/README.md) | 静的ライブラリとビルド手順 |

### 使い方

関数だけを含むファイルは、処理の開始点となる `main` 関数から呼び出します。C01・C03〜C06・C09には、Makefileと実行例を用意しています。C00・C02・C07・C08は実装途中の演習を含みます。

```sh
cd C06
make
make run EX=ex03 ARGS="banana apple cherry"
```
