yt-dlp_guiをダウンロードしていただきありがとうございます。
CUIの操作のみでしか使えなかったyt-dlpをGUIで動かすことによって使いやすくするするためのソフトになります。

＊＊特徴＊＊
・コマンドラインの知識がなくても、ボタン操作で動画をダウンロード可能  
・yt-dlp と ffmpeg を利用して高品質な動画・音声のダウンロードが可能  
・シンプルでわかりやすい UI  

＊＊ファイルの中身＊＊
yt-dlp_gui/
│── yt_dlp_gui.exe  （実行ファイル）
│── yt_dlp_gui.py   （ソースコード）
│── ffmpeg.exe      （GPL 版）
│── ffprobe.exe
│── yt-dlp.exe
│── LICENSE.txt     （GPL-3.0のライセンス文書）
│── README.txt      （ライセンス情報を記載）
│── VC_redist.x64.exe
 

＊＊動作環境＊＊
- Windows 10 / 11  
- Python 3.8 以上（ただし、実行ファイル版を使用する場合は Python は不要）  
- Visual Studio 2015 Visual C++（お使いの PC に入っていない場合のみインストールしてください）  

＊＊Visual Studio 2015 Visual C++ついて＊＊
Visual Studio 2015 Visual C++がインストールされていない場合、VC_redist.x64.exeをダブルクリックすることでダウンロードできます。必要に応じて使用してください。

＊＊使い方＊＊
1. `yt_dlp_gui.exe` をダブルクリック  
2. URL を入力  
3. ダウンロード形式（動画・音声）を選択  
4. ダウンロードボタンをクリック  

＊＊機能説明＊＊
- **～動画のURL～**  
  → 保存したい動画の URL を貼ってください。対応サイトは `yt-dlp supported sites` で検索してください。  
- **～保存先～**  
  → 保存場所を指定できます。  
- **～保存する形式～**  
  → 動画: mp4, mkv, webm / 音声: mp3, aac, flac, wav の中から選択できます。  
- **～ダウンロード～**  
  → 設定を選んでダウンロードボタンを押すと開始。完了するとボタンが元に戻ります。  

＊＊ライセンス＊＊
本ソフトウェアは **GNU General Public License v3.0 (GPL-3.0)** のもとで公開されています。

本アプリには、**ffmpeg** というオープンソースのソフトウェアを利用しています。ffmpegは、動画や音声の処理に使用され、**GNU Lesser General Public License (LGPL)** または **GNU General Public License (GPL)** のもとで提供されています。

ffmpeg のソースコードは以下のリンクから取得できます:  
[https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

ffmpegの使用に関するライセンス詳細は、[FFmpegのライセンスページ](https://ffmpeg.org/legal.html)をご確認ください。

※ **注意**: 本アプリに含まれるffmpegは、GPLライセンスに準拠したものを使用しています。利用にあたっては、ffmpegのライセンスに従っていただく必要があります。

＊＊ffmpegライセンス情報＊＊
- ffmpegのソースコードは、[こちら](https://ffmpeg.org/download.html)からダウンロードできます。
- このアプリには、ffmpegのビルド済み実行ファイル（ffmpeg.exe）が同梱されています。ffmpegは、動画や音声の変換やダウンロード処理に使用されます。
 
  

本アプリには ffmpeg を含めています。  
ffmpeg のソースコードは以下から取得できます:  
https://ffmpeg.org/download.html  

＊＊注意事項＊＊
- 本アプリは yt-dlp および ffmpeg を利用しています。これらのライセンスについても確認してください。  
- 本アプリを利用することによって生じた問題について、開発者は責任を負いません。  
- 著作権に注意し、合法的な範囲でご利用ください。  

＊＊開発者＊＊
rogawa  
X:@roooooooooogawa  

＊＊その他＊＊
本アプリは開発者が ChatGPT を活用して作成しました。  
何か問題や不具合がありましたらご連絡ください。
ソースコードは https://github.com/rogawa14/yt-dlp_guiで公開しています。  