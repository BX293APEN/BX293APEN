# Vim Cheat Sheet

![](https://www.plantuml.com/plantuml/png/bPFFIm915CVlyrUCDmtsq7KFOaJd3XsZWxHJBgXhEY8I7ToXr524e1Iqm2WmDhq4USWVVynprlelUjiQjQjcUXXtttxUvtrds8raU3JDiuau2V0OIp3AZJo9wHgZB97YUQgnp65QJt7TI194EQDWle2u0u5h6SGzY05Uq5D2yUSIylnHNZPbhJvvQpXbJu4gSNR4bJ05SGrc6ym741OKUfFnhUmsg4fpD1Z0Fpdeoz9hY90pGhpzQVquvWZsDmwGE_7XReHfl_FHlFY9ftfYkxvlrhtxpTetHTcjpoZ_-6mAPy_xT_Qs2N4YAGiVWoX-RVZ9sQqe4U975Ct89R7LCqobwZmONf1Ofy5fRIHR7Jn9C2sdRWvnr6HOdGvxKB3ioXYxGl-pHV-qRSwEPrG1ixgkUcj5qDvxksAth7MrnYgj_TnsvMXsLlDgBV_kAhyiLvVuYT-szFM9iAI6N-8d)

## 編集モード コマンド

### カーソル移動

<table>
    <tr>
        <th>コマンド</th>
        <th>説明</th>
    </tr>
    <tr>
        <td>
            <code>j</code> (or <code>↓</code>)
        </td>
        <td>
            下に移動
        </td>
    </tr>
    <tr>
        <td>
            <code>k</code> (or <code>↑</code>) 
        </td>
        <td>
            上に移動
        </td>
    </tr>
    <tr>
        <td>
            <code>h</code> (or <code>←</code>)
        </td>
        <td>
            左に移動
        </td>
    </tr>
    <tr>
        <td>
            <code>l</code> (or <code>→</code>)
        </td>
        <td>
            右に移動
        </td>
    </tr>
    <tr>
        <td>
            <code>w</code>
        </td>
        <td>
            次のスペース or 改行まで移動
        </td>
    </tr>
    <tr>
        <td>
            <code>b</code>
        </td>
        <td>
            前のスペース or 改行まで移動
        </td>
    </tr>
    <tr>
        <td>
            <code>gg</code>
        </td>
        <td>
            ファイルの先頭まで移動
        </td>
    </tr>
    <tr>
        <td>
            <code>G</code>
        </td>
        <td>
            ファイルの末尾行まで移動
        </td>
    </tr>
    <tr>
        <td>
            <code>0</code>
        </td>
        <td>
            行頭まで移動
        </td>
    </tr>
    <tr>
        <td>
            <code>$</code>
        </td>
        <td>
            行末へ移動
        </td>
    </tr>
    <tr>
        <td>
            <b>[文字数 (デフォルト : 1)]</b><code>|</code> 
        </td>
        <td>
            現在のカーソル位置から <b>[文字数]</b> 分、カーソル移動
        </td>
    </tr>

</table>


### 選択

<table>
    <tr>
        <th>コマンド</th>
        <th>説明</th>
    </tr>
    <tr>
        <td>
            <code>v</code>
        </td>
        <td>
            一文字ずつ選択(↑↓←→で選択範囲拡大)
        </td>
    </tr>
    <tr>
        <td>
            <code>V</code>
        </td>
        <td>
            一行ずつ選択(↑↓←→で選択範囲拡大)
        </td>
    </tr>
    <tr>
        <td>
            <code>ESC</code>
        </td>
        <td>
            解除
        </td>
    </tr>
</table>


### コピーペースト等

<table>
    <tr>
        <th>コマンド</th>
        <th>説明</th>
    </tr>
    <tr>
        <td>
            <b>[文字数 (デフォルト : 1)]</b><code>x</code>
        </td>
        <td>
            現在のカーソル位置から <b>[文字数]</b> 分、文字を切り取り
        </td>
    </tr>
    <tr>
        <td>
            <b>[文字数 (デフォルト : 1)]</b><code>yl</code>
        </td>
        <td>
            現在のカーソル位置から <b>[文字数]</b> 分、文字をコピー
        </td>
    </tr>
    <tr>
        <td>
            <b>[行数 (デフォルト : 1)]</b><code>dd</code>
        </td>
        <td>
            現在のカーソル位置から <b>[行数]</b> 分、行を切り取り
        </td>
    </tr>
    <tr>
        <td>
            <b>[行数 (デフォルト : 1)]</b><code>yy</code>
        </td>
        <td>
            現在のカーソル位置から <b>[行数]</b> 分、行をコピー
        </td>
    </tr>
    <tr>
        <td>
            <b>[回数 (デフォルト : 1)]</b><code>p</code>
        </td>
        <td>
            現在のカーソル位置の次の位置(行の場合 : 次の行)から <b>[回数]</b> 分、切り取った文字を貼り付け
        </td>
    </tr>
    <tr>
        <td>
            <b>[回数 (デフォルト : 1)]</b><code>P</code>
        </td>
        <td>
            現在のカーソル位置(行の場合 : カーソルの行の先頭)から <b>[回数]</b> 分、切り取った文字を貼り付け
        </td>
    </tr>

</table>

### Redo / Undo

<table>
    <tr>
        <th>コマンド</th>
        <th>説明</th>
    </tr>
    <tr>
        <td>
            <code>u</code>
        </td>
        <td>
            Undo 直前の変更を元に戻す
        </td>
    </tr>
    <tr>
        <td>
            <code>Ctrl</code> + <code>r</code>
        </td>
        <td>
            Redo
        </td>
    </tr>
</table>

### 検索

<table>
    <tr>
        <th>コマンド</th>
        <th>説明</th>
    </tr>
    <tr>
        <td>
            <code>/<正規表現文字列></code> 
        </td>
        <td>
            <code><正規表現文字列></code>を上から下へ検索
        </td>
    </tr>
    <tr>
        <td>
            <code>n</code>
        </td>
        <td>
            次を検索
        </td>
    </tr>
    <tr>
        <td>
            <code>N</code>
        </td>
        <td>
            前を検索
        </td>
    </tr>
</table>

### 置換

<table>
    <tr>
        <th>コマンド</th>
        <th>説明</th>
    </tr>
    <tr>
        <td>
            <code>:%s;<置換前文字列>;<置換後文字列></code>
        </td>
        <td>
            <code><置換前文字列></code>を<code><置換後文字列></code>に全て変更
        </td>
    </tr>
    <tr>
        <td>
            <code>:%s/<置換前文字列>/<置換後文字列></code>
        </td>
        <td>
            <code><置換前文字列></code>を<code><置換後文字列></code>に全て変更
        </td>
    </tr>
</table>
