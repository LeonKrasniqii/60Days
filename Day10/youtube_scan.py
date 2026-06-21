import yt_dlp
import csv
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

CHANNEL_URL = "https://www.youtube.com/channel/UCCml60xLLEi9Z_l8aKKUSqw/videos"

PATTERNS = [
    r"lyrics?\s*&\s*music\s*:?\s*edi krasniqi",
    r"lyrics?\s*/\s*music\s*:?\s*edi krasniqi",
    r"tekst\s*&\s*muzik\s*:?\s*edi krasniqi",
    r"teksti\s*&\s*muzika\s*:?\s*edi krasniqi",
    r"teksti\s*dhe\s*muzika\s*:?\s*edi krasniqi",
    r"music\s*&\s*video\s*-\s*edientertainment",
]

OUTPUT_FILE = "edi_krasniqi_songs.csv"


def check_video(video):
    try:
        title = video.get("title", "")
        video_id = video.get("id")

        if not video_id:
            return None

        url = f"https://www.youtube.com/watch?v={video_id}"

        ydl_opts = {
            "quiet": True,
            "skip_download": True,
            "no_warnings": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        description = (info.get("description") or "").lower()

        for pattern in PATTERNS:
            if re.search(pattern, description):
                return [title, url]

        return None

    except Exception:
        return None


def main():
    print("Loading channel...\n")

    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "skip_download": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(CHANNEL_URL, download=False)

    videos = info.get("entries", [])

    print(f"Found {len(videos)} videos")
    print("Scanning descriptions...\n")

    results = []

    # 15 parallel workers = much faster
    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = {
            executor.submit(check_video, video): video
            for video in videos if video
        }

        completed = 0

        for future in as_completed(futures):
            completed += 1

            result = future.result()

            if result:
                print(f"✔ MATCH: {result[0]}")
                results.append(result)

            if completed % 10 == 0:
                print(f"Progress: {completed}/{len(videos)}")

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["Song Title", "Video Link"])
        writer.writerows(results)

    print("\n======================")
    print(f"Done! Found {len(results)} songs")
    print(f"Saved to: {OUTPUT_FILE}")
    print("======================")


if __name__ == "__main__":
    main()