# YouTube Playlist to MP3 Downloader

Downloads YouTube playlists and converts them to MP3 at 192 kbps using `yt-dlp` and FFmpeg.

---

## Requirements

- Python 3.12+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Google Chrome (logged into YouTube — used for cookies to bypass age restrictions)

> **FFmpeg must be installed and added to your system PATH.**
> Without it the audio conversion step will fail and no MP3 files will be produced.
> Download FFmpeg from https://ffmpeg.org/download.html, extract it, and add the `bin/` folder to your PATH.
> You can verify it is working by running `ffmpeg -version` in a terminal.

---

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/caraus37/work.git
cd work
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install yt-dlp
```

**4. Configure the output directory**

Copy the template and edit it:

```bash
cp converter/variab.py.template converter/variab.py
```

Open `converter/variab.py` and set `BASE_PATH` to the folder where you want your MP3s saved:

```python
BASE_PATH = r"C:/Users/YourName/Music/YouTube/"
```

**5. Add your playlist URLs**

Open `converter/youtube-toMp3.py` and populate the `playlist_urls` list:

```python
playlist_urls = [
    "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID",
    "https://www.youtube.com/playlist?list=ANOTHER_PLAYLIST_ID",
]
```

---

## Running

```bash
.venv\Scripts\python converter\youtube-toMp3.py
```

---

## Output

| Path | Contents |
|------|----------|
| `<BASE_PATH>/music/` | Downloaded MP3 files |
| `<BASE_PATH>/download_log.txt` | Timestamped log of each session |
| `<BASE_PATH>/downloaded.txt` | Archive of already-downloaded video IDs |

Already-downloaded tracks are skipped automatically on subsequent runs. Delete `downloaded.txt` to force a full re-download.

---

## Notes

- By default, cookies are read from **Chrome**. Change `"cookiesfrombrowser": ("chrome",)` to `"firefox"` or `"edge"` in `youtube-toMp3.py` if needed.
- The script adds a small delay between playlists to avoid rate limiting.
