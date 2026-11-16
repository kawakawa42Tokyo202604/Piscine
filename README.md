# Piscine

## English

Programs and scripts written during the 42 Tokyo admission period, called the Piscine. They cover basic C functions, terminal file operations, and small team projects.

C exercises are grouped by topic; team projects are under `Rush`. For example, Rush01 solves a puzzle, while BSQ finds the largest obstacle-free square.

### Exercises

| Directory | Contents |
| --- | --- |
| [C](C/README.md) | Output, pointers, strings, recursion, dynamic memory, and headers |
| [Shell](Shell/README.md) | Files, permissions, Git, and text processing |
| [Rush](Rush/README.md) | Rectangles, a building-visibility puzzle, and number-to-English conversion |
| [BSQ](BSQ/README.md) | Find the largest square that avoids obstacles |

### Usage

C exercises are function-level sources; Rush and BSQ are executable programs. Each exercise directory contains its build commands and examples.

```sh
cd BSQ
make
```

### Tests

```sh
make test
```

Run `make test` at the repository root to build and test BSQ and Rush00–02. These tests cover executable behavior and input errors; they do not grade every C and Shell exercise. A C compiler, Python 3, and Make are required.

## 日本語

42 Tokyoの入学選考期間「Piscine」で取り組んだプログラムとスクリプトの記録です。Cの基本的な関数、端末でのファイル操作、チームで作る小さなプログラムを収録しています。

Cの演習はテーマ別に、チーム課題は `Rush` に分けています。例えばRush01はパズルの解答を探し、BSQは障害物のない最大の正方形を見つけます。

### 課題

| ディレクトリ | 内容 |
| --- | --- |
| [C](C/README.md) | 出力・ポインタ・文字列・再帰・動的メモリ・ヘッダー |
| [Shell](Shell/README.md) | ファイル操作・権限・Git・テキスト処理 |
| [Rush](Rush/README.md) | 長方形の描画、ビルの見え方を条件にしたパズル、数値の英語表記 |
| [BSQ](BSQ/README.md) | 障害物を避けて配置できる最大の正方形を探索 |

### 使い方

Cの演習は関数単位のファイル、Rush・BSQは実行プログラムです。ビルド方法と入力例は各課題の README に記載しています。

```sh
cd BSQ
make
```

### テスト

```sh
make test
```

リポジトリ直下の `make test` でBSQ・Rush00〜02をビルドして検証します。実行結果と入力エラーが対象で、C・Shellの全演習を採点するものではありません。Cコンパイラ・Python 3・Makeが必要です。
