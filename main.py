import os

def generate_index_html():
    output_dir = './dist'
    output_file = os.path.join(output_dir, 'index.html')
    
    os.makedirs(output_dir, exist_ok=True)
    print(f"ディレクトリ {output_dir} を確認/作成しました。")

    html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width" />
    <link href="./style.css" rel="stylesheet">
    <script src="https://unpkg.com/tone@14.8.49/build/Tone.js"></script>
    <title>Dynamic-Ratio-Tuner</title>
</head>
<body class="bg-indigo-100 text-blue-700">
	<main class="text-center">
		<h1 class="text-4xl m-10">Dynamic Ratio Tuner</h1>
		<div class="flex justify-center">
			<div id="pre_hz_id" class="m-10 text-3xl">440 Hz</div>
			<div class="m-10 text-3xl">→</div>
			<div id="now_hz_id" class="m-10 text-3xl">440 Hz</div>
		</div>
		<div class="width-full m-10 border border-solid border-blue-700"></div>
		<div id="keys_view" class="flex justify-center">
        <table class="border-separate">
"""
    #b. キーボードの描画
    frequencies = [ 1,1, 2,1, 3,2, 4,3, 5,4, 5,3, 6,5, 7,6, 7,5, 7,4, 8,7, 8,5, 9,8, 9,7, 9,5,
        10,9, 10,7, 11,10, 11,9, 11,8, 11,7, 11,6, 12,11, 12,7, 1,2, 2,3, 3,4, 3,5, 4,5, 4,7, 5,6, 5,7,
        5,8, 5,9, 6,7, 7,8, 7,9, 7,10, 7,11, 7,12, 7,13, 8,9, 8,11, 8,13, 9,10, 9,11, 9,13]
    keyLayout = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "^", "\\"
		,"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "@", "["
        , "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", ":", "]",
         "z", "x", "c", "v", "b", "n", "m", ",", ".", "/",
	]
    limit = [13,12,12,10]
    keyboard_html =""

    for i in range(4):
        keyboard_structure = "<tr>"
        for j in range(limit[i]+1):
            if j==0:
                colspan=i+1
                keyboard_structure += f'<td colspan="{colspan}"></td>'
            else:
                index = i*13+j-1-max(i-1,0)
                key=keyLayout[index]
                freq_data= f"{frequencies[index * 2]}/{frequencies[index * 2 + 1]}"
                tdcontent = f'{key}<br>{freq_data}'
                td_tag = f'<td colspan="2" class="border border-solid rounded-lg border-blue-700" id="{key}">{tdcontent}</td>'
                keyboard_structure += td_tag
        keyboard_structure += '<tr>'
        keyboard_html += keyboard_structure

    
    # c. フッターと結合
    html_content += keyboard_html
    html_content += """
    </table>
    </div>
		<div id="buttons" class="flex justify-center">
			<input type="button" value="Sine" id="Sine" class="border border-solid rounded-lg border-blue-700 m-5">
			<input type="button" value="Triangle" id="Triangle" class="border border-solid rounded-lg border-blue-700 m-5">
			<input type="button" value="Square" id="Square" class="border border-solid rounded-lg border-blue-700 m-5">
			<input type="button" value="Sawtooth" id="Sawtooth" class="border border-solid rounded-lg border-blue-700 m-5">
		</div>
	</main>	
    <script type="text/javascript" src='./script.js'></script>
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
    generate_index_html()