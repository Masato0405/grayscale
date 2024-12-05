Pythonの練習用に作った画像をグレースケールにするプログラムです。

Python3.12で動かしてます。

①コンテナの起動
`docker compose up -d`

②コンテナの中でライブラリのインストール
`cd /workspace`
`pip install -r requirements.txt`


③実行
`python grayscale-converter.py 画像のパス`

outputディレクトリに変換後の画像が保存されます。