print("-----文字列の中に含まれる文字が数を表す文字かどうかを判定する際に使用するメソッド-----")
print('\n', end='')
print("1.isdecimal（すべての文字が10進数で扱われる場合「真」とする）") #decimal : デシマル（10進数）を意味します
print("19920809".isdecimal())
print("19920809A".isdecimal())
print("1992/08/09".isdecimal())             # /
print("1992-08-09".isdecimal())             # -
print("1992,08,09".isdecimal())             # ,
print("1992 08 09".isdecimal())             # 空白
print("千九百九十二八九".isdecimal())       # 漢数字
print("⑤⑥⑦".isdecimal())                 # 環境依存字
print('\n', end='')
print("2.isdigit（すべての文字が数字の文字であれば「真」とする）")
print("19920809".isdigit())
print("19920809A".isdigit())
print("1992/08/09".isdigit())             # /
print("1992-08-09".isdigit())             # -
print("1992,08,09".isdigit())             # ,
print("1992 08 09".isdigit())             # 空白
print("千九百九十二八九".isdigit())       # 漢数字
print("⑤⑥⑦".isdigit())                 # 環境依存字(trueになります)
print('\n', end='')
print("3.isnumeric（すべての文字が数の文字であれば「真」とする）")
print("19920809".isnumeric())
print("19920809A".isnumeric())
print("1992/08/09".isnumeric())             # /
print("1992-08-09".isnumeric())             # -
print("1992,08,09".isnumeric())             # ,
print("1992 08 09".isnumeric())             # 空白
print("千九百九十二八九".isnumeric())       # 漢数字(trueになります)
print("⑤⑥⑦".isnumeric())                 # 環境依存字(trueになります)
