print("-----文字列を指定した区切り文字で分割し、分割された文字列をそれぞれ要素とするリストとして取得する-----")
print('\n', end='')
print('\n', end='')
print("1.split（指定した区切り文字で分割し、且つリストとして取得します）")
print("ccent ccna ccnp".split())          #区切り文字=空白
print("ccent,ccna,ccnp".split(","))       #区切り文字=,
print("ccent*-*ccna*-*ccnp".split("*-*")) #区切り文字=空白
print("ccent\tccna\tccnp".split("-"))     #区切り文字=\t
print("ccent  ccna  ccnp".split(" "))     #区切り文字=空白(明示的に指定)
print('\n', end='')
print("☆最大分割数の指定を行う☆")
print("A B C D E".split(" "))             #
print("A B C D E".split(" ", 1))          #最大分割数=1 文字列数=2
print("A B C D E".split(" ", 2))          #最大分割数=2 文字列数=3
print("A B C D E".split(" ", 3))          #最大分割数=3 文字列数=4
print("A B C D E".split(" ", 4))          #最大分割数=4 文字列数=5
print("A B C D E".split(" ", 5))          #最大分割数=5 文字列数=6
print("A B C D E".split(" ", 100000))     #最大分割数=100000 文字列数=100001
print('\n', end='')
print('\n', end='')
print("2.splitlines（改行文字を区切り文字として分割し、且つリストとして取得します）")
str1 = "Orange\nLmon\nApple"              #出力する際に、改行(\n)されて表示されるよう予め定義
print(str1)
print(str1.splitlines())                  #改行文字(\n)を区切り文字として分割
print('\n', end='')
msg1 = "Orange\nLmon\nApple"              #出力する際に、改行(\n)されて表示されるよう予め定義
print(msg1)
print(msg1.splitlines(True))              #引数に「True」を指定することで、区切り文字も含めて分割を行う
