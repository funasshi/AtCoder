## 事前準備
まずはpoetry環境に入る。

```
poetry shell
```
次に、ライブラリを使用するためにatcoderのログインが2つ必要
```
acc login
oj login https://beta.atcoder.jp/
```
## 問題のダウンロード
```
acc new {問題のid}
```
↑により、問題フォルダがダウンロードされる。問題フォルダは↑コードを打ったディレクトリに入るため、src内で打つのが推奨

例
```
acc new abc334
```

## 提出方法
提出問題のファイルに移動

例
`
cd src/abc211/a
`

sbコマンドを打つ

例 
```
sb //PyPy
sb2 //Python
```

