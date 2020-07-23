import tkinter as tk                    
import random

#おみくじ関数の定義
def omikuji():
    list_kuji =  ['大吉','吉','中吉','小吉','末吉','凶','大凶']
    result = random.choice(list_kuji)   # list_kujiからランダムに抽出
    response_area.configure(text=result)

#=================================================
# 画面描画用の関数
#=================================================

def run():
    global response_area   #グローバル変数を使用するための記述
    root = tk.Tk()         #メインウィンドウを作成
    root.title('おみくじ')   #ウィンドウタイトルを設定
    
    #キャンバスの作成
    canvas = tk.Canvas(width = 600,height = 400)
    canvas.pack()
    img = tk.PhotoImage(file = 'img1.gif')
    canvas.create_image(0,0,image = img,anchor = tk.NW)
    
    #応答エリアを作成
    response_area = tk.Label(width=66,height=5,bg='gray')
    response_area.pack()
    
    #ボタンの作成
    button = tk.Button(text='  おみくじ　　',command=omikuji)
    button.pack()
    
    def fix():
        a = root.winfo_geometry().split('+')[0]
        b = a.split('x')
        w = int(b[0])
        h = int(b[1])
        root.geometry('%dx%d' % (w+1,h+1))
    root.update()
    root.after(0, fix)
    
    #メインループ
    root.mainloop()

#=================================================
# プログラムの起点
#=================================================

if __name__  == '__main__':
    run()
