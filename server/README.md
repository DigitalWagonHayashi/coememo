# fairy-wise 裏処理
## 1. 概要
子機からの音声データの受け取りや推論を管理する

## 2. 機能
- 子機からの音声データの受け取り
- 音声データの保存
- 推論の実行
- 推論結果の保存
- 推論結果の窓口

## 3. 技術スタック
- Python
  - fastapi
  - sqlalchemy
  - openai-whisper

## 4. ディレクトリ構成
```
fairy-wise
├── README.md
├── main.py
├── Pipfile
├── Pipfile.lock
├── core
│   ├── inference
│   │   ├── modules
│   │   │   ├── models.py
│   │   └── inference.py
├── db
│   ├── common.py
│   ├── models.py
│   ├── initialize.py
│   └── crud.py
├── server
│   ├── app_instance.py
│   ├── routes.py
│   └── schemas.py
└── tests
    ├── test_main.py
    ├── test_db.py
    └── test_server.py
```


