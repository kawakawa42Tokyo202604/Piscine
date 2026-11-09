# Shell 00

## English

Exercises in terminal file operations and basic Git usage. They cover archives that preserve file attributes, file listings, and commit history.

Each `ex*` contains the resulting files or commands. For example, `ex05/git_commit.sh` prints the identifiers (hashes) of the five most recent commits in the repository where it runs.

### Contents

| Location | Contents |
| --- | --- |
| `ex00` | A text file with specified contents |
| `ex01` / `ex02` | tar archives including file attributes |
| `ex03` | A public key file |
| `ex04/midLS` | File listing ordered by modification time |
| `ex05/git_commit.sh` | The five most recent commit hashes |
| `ex06/git_ignore.sh` | Untracked files ignored by Git |
| `ex07` | Files used for comparison |
| `ex08/clean` | Find and remove files matching `*~` or `#*#` |
| `ex09/ft_magic` | Detect a file using text at a specified offset |

### Examples

```sh
sh ex04/midLS
sh ex05/git_commit.sh
```

Run the Git exercises inside a Git repository. `ex08/clean` removes matching files beneath its working directory.

`make` checks script syntax; `make run` runs `ex04/midLS`. Set `SCRIPT` to select another script.

## 日本語

端末でのファイル操作とGitの基本を試す演習です。属性を保ったアーカイブの作成や、ファイル一覧・コミット履歴の表示などを扱います。

各 `ex*` に、作成したファイルやコマンドを保存しています。例えば `ex05/git_commit.sh` は、実行したGitリポジトリの直近5件のコミットを識別する文字列（ハッシュ）を表示します。

### 内容

| 場所 | 内容 |
| --- | --- |
| `ex00` | 指定内容のテキストファイル |
| `ex01` / `ex02` | ファイル属性を含むtarアーカイブ |
| `ex03` | 公開鍵ファイル |
| `ex04/midLS` | 更新日時順のファイル一覧 |
| `ex05/git_commit.sh` | 直近5件のコミットハッシュ |
| `ex06/git_ignore.sh` | Gitが無視する未追跡ファイル |
| `ex07` | 比較用のファイル |
| `ex08/clean` | `*~`・`#*#` に一致するファイルの検索・削除 |
| `ex09/ft_magic` | 指定位置の文字列でファイルを判定するルール |

### 実行例

```sh
sh ex04/midLS
sh ex05/git_commit.sh
```

Gitの演習はGitリポジトリ内で実行します。`ex08/clean` は実行した場所の配下から該当ファイルを削除するコマンドです。

`make` でスクリプトの構文を確認し、`make run` で `ex04/midLS` を実行できます。`SCRIPT` で別のスクリプトを選べます。
