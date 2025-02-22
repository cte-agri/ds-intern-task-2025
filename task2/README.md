## Task2

あなたはキュウリとトマトとナスを育てている農家です。収穫した野菜を重さを基準とした規格別に選別しました。
このとき、個数比でキュウリ：トマト：ナス=4:3:3でした。

そこから何個かランダムに取り出して袋に詰めていきます。
袋の中の野菜の価格合計がある一定の金額上限を超えたとき、越えた分は袋に入れず、金額上限以下になるように袋詰めを終了します。このとき、再度取り出すことはしません。
ただし、金額上限に達していなくても、袋に入る個数の最大値は30個です。

毎日、袋は10個つくります。袋詰めを終了する金額上限は日によって変わります。

ある日の10袋のキュウリ・トマト・ナスそれぞれの個数が与えられますので、その日の金額上限を推定してください。

野菜の重さは以下の正規分布に従います：
- キュウリ：平均100、標準偏差20
- トマト：平均150、標準偏差15
- ナス：平均180、標準偏差18

<規格表>
|        | S         | M         | L         |
|--------|-----------|-----------|-----------|
| キュウリ | 51-80     | 81-120    | 121-150   |
| トマト   | 101-135   | 136-165   | 166-200   |
| ナス     | -         | 161-200   | 201-240   |
- ナスはM・Lサイズのみとなります。
- 規格表の範囲でないものは規格外品となります。

<価格表>
|        | S         | M         | L         | 規格外         |
|--------|-----------|-----------|-----------|-----------|
| キュウリ | 30   | 60   | 60   | 0   |
| トマト   | 50   | 100   | 150   | 10   |
| ナス     | -         | 120   | 180   | 0   |


入力はランダムに生成されています。また、野菜の重さはそれぞれ整数値とします。

## 入力
プログラムに、以下のフォーマットの標準入力が与えられます。
```plain
C1 T1 E1
C2 T2 E2
...
C10 T10 E10
```
Ci は i 個目の袋の中のキュウリの個数、
Ti は i 個目の袋の中のトマトの個数、
Ei は i 個目の袋の中のナスの個数を表します。

制約は以下です。
- Ci, Ti, Ei  は整数
- Ci, Ti, Ei >= 0
- Ci + Ti + Ei <= 20

## 出力
その日の金額上限を標準出力に出力してください。
金額上限は整数であり、500円以上3,000円以下です。

##  評価
評価には、平均絶対値誤差 $MAE$と処理時間を $T$を用いて表される $\ln(\text{MAE} \times T )$の値を評価指標の参考値として用います。

**ただし、この問題では想定したアルゴリズムであっても必ずしも満点（誤差0）を取れません。点数よりもどのような理論や発想に基づいているかを評価します。**


## 入出力例
### 例 1
標準入力
```plain
3 3 4
7 0 3
4 2 3
6 2 2
5 1 3
3 3 3
7 0 4
10 1 1
5 3 4
3 2 4
```
標準出力
```plain
854
```

### 例 2
標準入力
```plain
3 8 5
6 6 4
8 6 8
5 3 8
9 4 5
5 4 6
11 3 5
9 5 5
8 3 8
15 3 4
```
標準出力
```plain
1545
```
