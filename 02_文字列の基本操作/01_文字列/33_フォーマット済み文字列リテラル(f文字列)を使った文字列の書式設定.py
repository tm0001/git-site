print("python 3.6 から、フォーマット済み文字列リテラル(f文字列)が利用できるようになりました")
print('\n', end='')
print('\n', end='')
print("-----1.フォーマット済み文字列リテラルの記述方法-----")
print('\n', end='')
print("❶formatメソッドを用いて表現する場合")
name = "Takeuchi"
old = 27
print("名前は{:<8s}です。年齢は{:>3d}歳になります。" .format(name, old))
print('\n', end='')
print("❷フォーマット済み文字列を用いて表現する場合")
name = "Takeuchi"
old = 27
print(f"名前は{{ {name:<8s} }}です。年齢は{{ {old:>3d} }}歳になります。")
print('\n', end='')
print('\n', end='')
print("-----2.書式指定子の指定方法-----")
print('\n', end='')
num = 0.0752
print("❶指数表記")
print(f"指数表記={num:e}")
print('\n', end='')
print("❷固定小数点表記")
print(f"固定小数点表記={num:f}")
print('\n', end='')
print("❸パーセンテージ表記")
print(f"パーセンテージ表記={num:%}")
print('\n', end='')
print("❹最小フィールドの幅の指定と配置方法 ※前項までと表記が少し異なります")
str1 = "LEMON"
print(f"文字列=[{str1:<10s}]")
print(f"文字列=[{str1:^10s}]")
print(f"文字列=[{str1:>10s}]")
print('\n', end='')
print("❺数値の区切り文字 ※数値の千の位で区切り文字を挿入します")
num = 1234567
print(f"数値={num:,d}")
