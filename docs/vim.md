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
            `j` (or `↓`)
        </td>
        <td>
            下に移動
        </td>
    </tr>
    <tr>
        <td>
            `k` (or `↑`) 
        </td>
        <td>
            上に移動
        </td>
    </tr>
    <tr>
        <td>
            `h` (or `←`)
        </td>
        <td>
            左に移動
        </td>
    </tr>
    <tr>
        <td>
            `l` (or `→`)
        </td>
        <td>
            右に移動
        </td>
    </tr>
    <tr>
        <td>
            `w`
        </td>
        <td>
            次のスペース or 改行まで移動
        </td>
    </tr>
    <tr>
        <td>
            `b`
        </td>
        <td>
            前のスペース or 改行まで移動
        </td>
    </tr>
    <tr>
        <td>
            `gg`
        </td>
        <td>
            ファイルの先頭まで移動
        </td>
    </tr>
    <tr>
        <td>
            `G`
        </td>
        <td>
            ファイルの末尾行まで移動
        </td>
    </tr>
    <tr>
        <td>
            `0`
        </td>
        <td>
            行頭まで移動
        </td>
    </tr>
    <tr>
        <td>
            `$`
        </td>
        <td>
            行末へ移動
        </td>
    </tr>
    <tr>
        <td>
            **[文字数 (デフォルト : 1)]**`|` 
        </td>
        <td>
            現在のカーソル位置から **[文字数]** 分、カーソル移動
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
            `v`
        </td>
        <td>
            一文字ずつ選択(↑↓←→で選択範囲拡大)
        </td>
    </tr>
    <tr>
        <td>
            `V`
        </td>
        <td>
            一行ずつ選択(↑↓←→で選択範囲拡大)
        </td>
    </tr>
    <tr>
        <td>
            `ESC`
        </td>
        <td>
            解除
        </td>
    </tr>
</table>


### コピーペースト等
| コマンド | 説明 |
| --- | --- |
| **[文字数 (デフォルト : 1)]**`x` | 現在のカーソル位置から **[文字数]** 分、文字を切り取り |
| **[文字数 (デフォルト : 1)]**`yl` | 現在のカーソル位置から **[文字数]** 分、文字をコピー |
| **[行数 (デフォルト : 1)]**`dd` | 現在のカーソル位置から **[行数]** 分、行を切り取り |
| **[行数 (デフォルト : 1)]**`yy` | 現在のカーソル位置から **[行数]** 分、行をコピー |
| **[回数 (デフォルト : 1)]**`p` | 現在のカーソル位置の次の位置(行の場合 : 次の行)から **[回数]** 分、切り取った文字を貼り付け |
| **[回数 (デフォルト : 1)]**`P` | 現在のカーソル位置(行の場合 : カーソルの行の先頭)から **[回数]** 分、切り取った文字を貼り付け |

### Redo / Undo

<table>
    <tr>
        <th>コマンド</th>
        <th>説明</th>
    </tr>
    <tr>
        <td>
            `u`
        </td>
        <td>
            Undo 直前の変更を元に戻す
        </td>
    </tr>
    <tr>
        <td>
            `Ctrl` + `r`
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
            `/<正規表現文字列>` 
        </td>
        <td>
            `<正規表現文字列>`を上から下へ検索
        </td>
    </tr>
    <tr>
        <td>
            `n`
        </td>
        <td>
            次を検索
        </td>
    </tr>
    <tr>
        <td>
            `N`
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
            `:%s;<置換前文字列>;<置換後文字列>`
        </td>
        <td>
            <置換前文字列>を<置換後文字列>に全て変更
        </td>
    </tr>
    <tr>
        <td>
            `:%s/<置換前文字列>/<置換後文字列>`
        </td>
        <td>
            <置換前文字列>を<置換後文字列>に全て変更
        </td>
    </tr>
</table>
