# Flask + MongoDB で REST API (CRUD) 

- [MongoDB Community Server](https://www.mongodb.com/try/download/community) をローカルで動かして開発。
- MongoDB Atlas に接続する場合は `server.py` のコメントアウト参照

## 📝開発環境

- MongoDB 4.4.1 Community Server
- Python 3.8.6
- Flask 1.1.2
- pymongo 3.11.0

## 📝API エンドポイント

|method|path|-|
|---|---|---|
|GET|/users|全ユーザーの情報を取得|
|POST|/users|ユーザーの登録|
|PATCH|/users/ユーザーID|ユーザーの情報を更新|
|DELETE|/users/ユーザーID|ユーザーを削除|

## 📝プロジェクトディレクトリの作成

```bash
mkdir flask-mongo-1
cd flask-mongo-1
```

## 📝Python 仮想環境の作成

### 🔖プロジェクト直下に仮想環境を作成したい場合の設定

~/.bashrc

```text
# .venv をプロジェクトローカルに作る
export PIPENV_VENV_IN_PROJECT=true
```

### 🔖仮想環境の作成

```bash
pipenv --python 3.8.6
```

## 📝ライブラリのインストール

```bash
pipenv install flask
pipenv install pymongo
pipenv install dnspython
pipenv install python-dotenv
```

## 📝動作確認

```bash
python server.py
```

Postman で API にアクセスして動作確認