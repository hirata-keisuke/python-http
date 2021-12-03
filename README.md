# python-http

dockerとpythonの標準ライブラリを利用して、リクエストにレスポンスを返すWebサーバを実装します。

## パッケージhttp.serverを使った簡易なサーバ(version:1)

http.serverを実行するのみ、機能はリクエストを受けるだけです。

## 一緒に置いたindex.htmlを表示する(version:2)

socketserver.TCPServerを使います。

## GETとPOSTにレスポンスを定義する(version:3)

http.server.BaseHTTPRequestHandlerのサブクラスを作ります。

## 参考

- PythonによるHTTPサーバ立ち上げ  
https://www.lifewithpython.com/2021/03/python-https-server.html

- Pythonの標準ライブラリ(http.server)  
https://docs.python.org/ja/3/library/http.server.html#module-http.server

- クラスを自作して動作制御をする  
https://kazuhira-r.hatenablog.com/entry/2019/08/12/220406
