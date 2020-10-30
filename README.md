# README

## Description

- MongoDB へと CRUD を行う REST API を Flask で実装したサンプルプロジェクトです。

## Requirement

- [MongoDB 4.4.1 Community Server](https://www.mongodb.com/try/download/community)
- Python 3.8.6
- Flask 1.1.2
- pymongo 3.11.0

## REST API endpoint

|method|path|-|
|---|---|---|
|GET|/users|全ユーザーの情報を取得|
|POST|/users|ユーザーの登録|
|PATCH|/users/ユーザーID|ユーザーの情報を更新|
|DELETE|/users/ユーザーID|ユーザーを削除|

## Getting Started

### Clone

```bash
git clone https://github.com/kiyotd/sample-flask-rest-mongo-crud.git
```

### Creating a virtual environment and installing modules

```bash
cd flask-mongo-rest-crud
pipenv install
```

### Runs the app

```bash
pipenv run python server.py
```

[Postman](https://www.postman.com/downloads/) のインストールを行い、API のエンドポイントにリクエストを送信して動作を確認する。

### When connecting to the MongoDB Atlas

- `server.py` のコメントアウト参照


## Licence

The MIT License

## Author

**kiyotd**  
web designer, front-end engineer

- [kiyotd.com](https://kiyotd.com/)
- [twitter](https://twitter.com/_kiyotd)
- [github](https://github.com/kiyotd)