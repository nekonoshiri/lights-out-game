# lights-out-game

ライツアウト風のゲーム。

## インストールと起動

1. [Poetry](https://github.com/python-poetry/poetry) をインストール。
2. `poetry install` で依存パッケージをインストール。
3. `poetry run lights_out_game` でゲームを起動。

※ うまくいかない場合は以下の手順でも起動できます。

1. `pip3 install .`
2. `lights_out_game`

## 構成

### ソースコード

- `lights_out_game/`: メインソースコード。
- `test/`: テストソースコード。

### Python パッケージ関連ファイル

- `pyproject.toml`: パッケージと依存関係の管理ファイル。
- `poetry.lock`: ロックファイル。Poetry による自動生成。

### その他

- `invoke.yaml`: Invoke の設定。
- `setup.cfg`: 各種開発用ツールの設定。
- `tasks.py`: Invoke のタスク定義。

