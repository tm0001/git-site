print("-----文字列の中に含まれ位置を取得する際に使用するメソッド-----")
print('\n', end='')
print('\n', end='')
print("1.find（文字列の中で指定した文字列が最初に現れるインデックスを取得 ※見つからない場合は「-1」を返す）")
print("devil may cry".find("ma"))      # 「ma」という文字列が最初に現れるインデックスは0から数えて6つ目 ※空白もカウントされる
print("Good School".find("oo"))        # 「oo」という文字列が最初に現れるインデックスは0から数えて1つ目 ※2つ目以降は合致しても無視する
print("Good School".find("oo", 3, 10)) # 検索するインデックスを指定しています。この場合、1番目の「oo」は無視されます
print("Good School".find("oo", 3))     # 範囲指定の終了位置を省略した場合、最後の文字列までを検索対象としてみなし検索を行います
print("Orange Color".find("ab"))       # findで指定した文字列が見つからなかった場合は-1が返される
print('\n', end='')
print('\n', end='')
print("2.index（文字列の中で指定した文字列が最初に現れるインデックスを取得 ※見つからない場合は「ValueError」を返す）")
print("devil may cry".index("ma"))
print("Good School".index("oo"))
print("Good School".index("oo", 3, 10))
# print("Orangr Color".index("oo")) # 左記コマンドを実行するとエラーになります
print('\n', end='')
print('\n', end='')
print("3.rfind（文字列の中で指定した文字列が最後に現れるインデックスを取得 ※見つからない場合は「-1」を返す）")
print("Good School".rfind("oo"))
print("Orange Color".rfind("zz"))
print('\n', end='')
print('\n', end='')
print("4.rindex（文字列の中で指定した文字列が最後に現れるインデックスを取得 ※見つからない場合は「ValueError」を返す）")
print("Good School".rindex("oo"))
# print("Orange Color".rindex("zz")) # 左記コマンドを実行するとエラーになります
