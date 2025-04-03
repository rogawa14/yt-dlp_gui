# yt-dlp_gui.py - yt-dlp の GUI フロントエンド
# Copyright (C) 2024 [rogawa]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


import tkinter as tk
from tkinter import filedialog
import subprocess

def download_video():
    # 入力されたURLと保存先、拡張子を取得
    url = entry_url.get()
    save_path = entry_save_path.get()
    ext = combo_ext.get()

    # 動画を音声に変換して保存する場合
    if ext in ["mp3", "aac", "flac", "wav"]:
        command = f"yt-dlp -o {save_path}/%(title)s.{ext} -f bestaudio {url}"
    else:
        command = f"yt-dlp -o {save_path}/%(title)s.{ext} {url}"

    # コマンド実行
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # 結果を表示
    label_result.config(text=result.stdout.strip() if result.stdout else result.stderr)

def browse_folder():
    # 保存先フォルダを選ぶダイアログ
    folder = filedialog.askdirectory()
    entry_save_path.delete(0, tk.END)  # 既存のテキストを消す
    entry_save_path.insert(0, folder)  # 新しいパスを挿入

# ウィンドウ作成
root = tk.Tk()
root.title("yt-dlp GUI")
root.geometry("500x300")

# URL入力欄
label_url = tk.Label(root, text="動画のURL:")
label_url.pack(pady=5)
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

# 保存先選択
label_save_path = tk.Label(root, text="保存先:")
label_save_path.pack(pady=5)
entry_save_path = tk.Entry(root, width=50)
entry_save_path.pack(pady=5)
button_browse = tk.Button(root, text="保存先選択", command=browse_folder)
button_browse.pack(pady=5)

# 拡張子選択
label_ext = tk.Label(root, text="保存する形式:")
label_ext.pack(pady=5)
combo_ext = tk.StringVar()
combo_ext.set("mp4")  # デフォルトはmp4
ext_dropdown = tk.OptionMenu(root, combo_ext, "mp4", "mkv", "webm", "mp3", "aac", "flac", "wav")
ext_dropdown.pack(pady=5)

# ダウンロードボタン
button_download = tk.Button(root, text="ダウンロード", command=download_video)
button_download.pack(pady=20)

# 結果表示用ラベル
label_result = tk.Label(root, text="ここに結果が表示されます")
label_result.pack(pady=5)

# ウィンドウを表示
root.mainloop()
