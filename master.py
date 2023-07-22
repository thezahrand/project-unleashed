#@title Download Section { vertical-output: true }
#@markdown <br><center><img src='https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg' height="50" alt="FFmpeg-logo"/></center>
#@markdown <center><h3>Download Youtube Video</h3></center><br>
print('---------------------------------------------------------------------------')
print('PACKAGE LOADING...')
!pip install -q yt-dlp
link = 'https://www.youtube.com/watch?v=JMiX9wRoM3s' #@param {type:"string"}
print('---------------------------------------------------------------------------')
print("ACCESSING ARGUMENTS...")
!yt-dlp -q --downloader aria2c --progress --downloader-args aria2c -f b $link
import yt_dlp
YDL_OPTIONS = {
    'noplaylist': True,
}
with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
    info = ydl.extract_info(link, download=False)
print('---------------------------------------------------------------------------')
print('DATA FILE:')
print(info['title'])
print('---------------------------------------------------------------------------')
print('DAH KEDOWNLOAD NEH!')
print('>> DOWNLOAD LAGI DI FILE BROWSER!')
print('---------------------------------------------------------------------------')
