# メモ
## gitコマンドの使い方
### ユーザ登録
```
git config --global user.name <名前>
git config --global user.email <メールアドレス>
```
#### 確認
* Windows 
```
git config --list | findstr "user.name"
```
* Linux
```
git config --list | grep "user.name"
```
### 初期化
```
git init
```
- .gitという隠しフォルダが生成される(このディレクトリ内での作業が可能になる)
### リモートリポジトリの指定  
```
git remote add origin <リポジトリのURL>
```
### メインブランチを指定  
```
git branch -M main
```
### アップロードしたいファイル指定
```
git add <ファイル名, ディレクトリ名, -A:全て>
```
### アップロードしたいファイルをコミット
```
git commit -m "コメント"
```
### ファイルのアップロード
```
git push -u origin main  // 初回のみ
git push
```
### ダウンロード
```
git clone <リポジトリのURL>
```
### ファイル復元
```
git restore <ファイル名, ディレクトリ名>
```
### Alias設定
```
git config --global alias.<新たに設定したいコマンド名> <gitコマンド>
```
→ ```git <新たに設定したいコマンド名>```を打つと```git <gitコマンド>```が実行される
### ログの確認
```
git log
git log - <確認したいログの数>
```
### ブランチ作成・移動
```
git switch -c <新しいブランチ名, 移動先ブランチ名>
```
### ブランチ合成
```
git merge <併合したいブランチ>
git merge --allow-unrelated-histories //履歴の異なるブランチを合成することを許可する
```
→ 自ブランチに<併合したいブランチ>が合成される
### ブランチ確認
```
git branch -a
```
### ローカルブランチ削除
```
git branch -d <削除したいブランチ> // 変更をマージした後実行可能
git branch -D　<過去の変更まで完全削除したいブランチ>
```
### 競合解決
```
git push -u origin main
```
