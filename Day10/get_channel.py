import yt_dlp

VIDEO_URL = "https://youtu.be/6ZdscitnoLs"

with yt_dlp.YoutubeDL({"quiet": False}) as ydl:
    info = ydl.extract_info(VIDEO_URL, download=False)

    print("Channel:", info.get("channel"))
    print("Channel ID:", info.get("channel_id"))
    print("Channel URL:", info.get("channel_url"))