import yt_dlp
import os
from datetime import datetime
import time
from variab import BASE_PATH

# === CONFIG ===
MUSIC_PATH = os.path.join(BASE_PATH, "music")
LOG_FILE = os.path.join(BASE_PATH, "download_log.txt")
ARCHIVE_FILE = os.path.join(BASE_PATH, "downloaded.txt")

os.makedirs(MUSIC_PATH, exist_ok=True)

playlist_urls = [
    "link to playlist"
]


# === LOGGING ===
def log_message(message):
    msg = f"{datetime.now():%Y-%m-%d %H:%M:%S} - {message}"
    print(msg)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


# === YT-DLP OPTIONS (LARGE PLAYLIST SAFE) ===
ydl_opts = {
    # Best audio only
    "format": "bestaudio/best",

    # Use video ID to avoid title mismatch issues
    "outtmpl": os.path.join(
        MUSIC_PATH, "%(title)s.%(ext)s"  # %(id)s -
    ),

    # avoid age restrictions
    "cookiesfrombrowser": ("chrome",),  # or "firefox", "edge", etc.

    # Convert to MP3
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],

    # Reliability
    "retries": 10,
    "fragment_retries": 10,
    "concurrent_fragment_downloads": 1,

    # Throttling protection
    "sleep_interval": 2,
    "max_sleep_interval": 5,

    # Resume & skip already downloaded
    "download_archive": ARCHIVE_FILE,

    # Stable client
    "player_client": "android",

    # Logging
    "quiet": True,
    "noprogress": True,
    "no_warnings": True,

    # Network safety
    "geo_bypass": True,
    "nocheckcertificate": True,
}

# === PLAYLIST DOWNLOAD ===


def download_playlist(url):
    log_message("Starting playlist download")
    log_message(url)

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        log_message("Playlist download finished successfully")

    except Exception as e:
        log_message(f"Playlist failed: {e}")


# === MAIN ===
if __name__ == "__main__":
    log_message("=== DOWNLOAD SESSION STARTED ===")

    for url in playlist_urls:
        download_playlist(url)
        time.sleep(3)  # small cooldown between playlists

    log_message("=== SESSION COMPLETE ===")
    print("\n Done. Check the log for details.")
