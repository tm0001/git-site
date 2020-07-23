print("置換フィールドに数値を指定する")
print('\n', end='')
print("名前は{0}です。今年で{1}歳になります。住所は{2}です。 ".format("Masato", 27, "Tokyo"))
print("名前は{}です。今年で{}歳になります。住所は{}です。 ".format("Masato", 27, "Tokyo"))
print('\n', end='')
print('\n', end='')
print("-----[書式指定子の指定方法]-----")
print('\n', end='')
print("1.type(値の表現型)")
print("数値01={:d}, 数値02={:x} " .format(20,31))
print("指数表記={:e}" .format(0.0752))
print("固定小数点表記={:f}" .format(0.0752))
print("パーセンテージ={:%}" .format(0.348))
print('\n', end='')
print('\n', end='')
print("2.width(最小フィールド幅 ※少なくとも確保される桁数を指定)")
print("文字列=[{:10s}], 数値=[{:5}]" .format("Lemon", 123))
print('\n', end='')
print('\n', end='')
print("3.fill(埋める文字)とalign(配置方法)")
print("数値=[{:<7d}]".format(123))
print("数値=[{:^7d}]".format(123))
print("数値=[{:>7d}]".format(123))
print("数値=[{:*<7d}]".format(123))
print("数値=[{:-^7d}]".format(123))
print('\n', end='')
print('\n', end='')
print("4.sign(符号) ※数値に対してのみ有効な設定です")
print("正の数={:+d}, 負の数={:+d}" .format(72, -72))  # + : 正の数、負の数ともに符号をつける
print("生の数={:-d}, 負の数={:-d}" .format(72, -72))  # - : 負の数だけに符号をつける
print("生の数={: d}, 負の数={: d}" .format(72, -72))  #   : 正の数の数値の前に空白をつける
print('\n', end='')
print('\n', end='')
print("5.grouping_option(数値の区切り文字)")
print("数値={:,d}" .format(1234567))     # 千の位ごとにカンマを挿入
print("数値={:,f}" .format(12345.6789))  # 千の位ごとにカンマを挿入（小数点も考慮する）
print("数値={:_d}".format(1234567))      # 千の位ごとにアンダーバーを挿入
print('\n', end='')
print('\n', end='')
print("6.precision(小数点の精度) ※少数部分の精度(桁数)を指定") # precision = 「精度」を意味する
print("数値={:f}" .format(1.2345))     # 桁数の指定なし（未指定の場合はデフォルトで6桁まで表示されます）
print("数値={:.1f}" .format(1.2345))   # 小数点第一位までを指定
print("数値={:.3f}" .format(1.2345))   # 小数点第三位までを指定
print('\n', end='')
print('\n', end='')
print("7.#(別形式)")
print("数値={:b}, 数値={:#b}" .format(10, 10))  # 2進数で表示
print("数値={:o}, 数値={:#o}" .format(20, 20))  # 8進数で表示
print("数値={:x}, 数値={:#x}" .format(35, 35))  # 16進数で表示
