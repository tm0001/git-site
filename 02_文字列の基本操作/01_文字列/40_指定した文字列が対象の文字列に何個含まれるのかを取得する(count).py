print("-----指定した文字列が対象の文字列に何個含まれるのかを取得する（count）-----")
print('\n', end='')
print('\n', end='')
print("devil may cry".count("ma"))
print("Good School".count("oo"))
print("Goooood idea".count("oo"))
print("Orange Color".count("zx"))
print("Good School".count("oo", 3, 10))  # 3~10文字目までの範囲で対象文字列の検索を行う
print("Good School".count("oo", 3))      # 数字1文字の指定は検索開始文字とみなされ、最後の文字列まで検索が行われる
print('\n', end='')
print("【*重要❶*】重複せずに現れる回数を返す → 重複した場合は無視されます")
print("【*重要❷*】検索対象の文字列が存在しない場合は0が返される ※「0個でした」という意味になります")
print("【*重要❸*】find, index と同様に、文字を検索する位置パラメータを指定することが可能です")
