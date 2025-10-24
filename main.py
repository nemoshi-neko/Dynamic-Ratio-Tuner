import os

def generate_hello_html():
    # 1. 出力ディレクトリとファイルパスの定義
    output_dir = './dist'
    output_file = os.path.join(output_dir, 'hello.html')
    
    # 2. ディレクトリの作成
    # exist_ok=True で、ディレクトリが既に存在していてもエラーにならないようにする
    os.makedirs(output_dir, exist_ok=True)
    print(f"ディレクトリ {output_dir} を確認/作成しました。")

    # 3. HTMLコンテンツの生成
    
    # a. 基本のHTMLヘッダー
    html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Hello 100 Times</title>
</head>
<body>
"""
    
    # b. <div>hello</div> を100回繰り返す（リスト内包表記とjoinを使用すると高速）
    div_line = "    <div>hello</div>" # インデントを考慮
    # 100回繰り返した文字列を改行で結合
    div_content = '\n'.join([div_line] * 100)
    
    # c. フッターと結合
    html_content += div_content
    html_content += """
</body>
</html>
"""

    # 4. ファイルへの書き込み
    try:
        # 'w'モードでファイルを開き、既存のコンテンツを上書き
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"ファイル {output_file} を正常に生成しました。")
        
    except IOError as e:
        print(f"ファイル書き込み中にエラーが発生しました: {e}")

if __name__ == "__main__":
    generate_hello_html()