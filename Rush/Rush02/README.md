# Rush 02

## English

A C program that converts an integer written in digits into English words. For example, `42` becomes `forty two`, and `1000` becomes `one thousand`.

Mappings from numbers to words are stored in `numbers.dict`. A different dictionary can change the wording for the same number.

### Build and run

Requires a C compiler and Make. Run from this directory so relative dictionary paths resolve correctly.

```sh
make
./rush-02 42
./rush-02 numbers.dict 1000
```

One argument uses the supplied `numbers.dict`. With two arguments, pass the dictionary path followed by the number.

### Implementation

Splits numbers into three-digit groups and reads words and scale units from the dictionary. Reports invalid numbers or dictionary problems with `Error` or `Dict Error`.

### Tests

```sh
make test
```

Checks zero, leading zeroes, digit boundaries, custom dictionaries, invalid numbers, and missing or incomplete dictionaries.

## 日本語

数字で渡された整数を、人が読む英語の表記に変換するCプログラムです。例えば `42` は `forty two`、`1000` は `one thousand` と表示します。

数と単語の対応は `numbers.dict` に保存しています。辞書を変えると、同じ数値に対して使う語を変更できます。

### ビルドと実行

Cコンパイラ・Make が必要です。辞書の相対パスを解決できるよう、このディレクトリで実行します。

```sh
make
./rush-02 42
./rush-02 numbers.dict 1000
```

引数が1個なら付属の `numbers.dict` を使い、2個なら辞書ファイル・数値の順で指定します。

### 実装メモ

数字を3桁ごとのまとまりに分け、対応する語と桁の単位を辞書から取り出します。不正な数値や辞書の不足は `Error`・`Dict Error` で知らせます。

### テスト

```sh
make test
```

0・先頭の0・桁の境界、独自辞書、不正な数値、存在しない辞書、不足した辞書を確認します。
