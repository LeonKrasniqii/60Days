import yt_dlp

url = "https://www.youtube.com/@EdiRifadija"

with yt_dlp.YoutubeDL({"quiet": False}) as ydl:
    info = ydl.extract_info(url, download=False)
    print(info.get("title"))