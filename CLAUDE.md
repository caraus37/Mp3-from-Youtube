# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A small Python utility that downloads YouTube playlists and converts them to MP3 using `yt_dlp` and FFmpeg.

## Environment

- Python 3.12, virtualenv at `.venv/`
- Run scripts with: `.venv\Scripts\python converter\youtube-toMp3.py`
- Install dependencies: `.venv\Scripts\pip install yt-dlp`
- FFmpeg must be installed and available on PATH for MP3 conversion

## Structure

- `converter/youtube-toMp3.py` — main script; reads playlist URLs, downloads audio, converts to MP3
- `converter/variab.py` — single constant `BASE_PATH` pointing to the output directory on disk

## Key Configuration

Before running, edit these two files:

1. **`converter/variab.py`** — set `BASE_PATH` to the desired output root directory
2. **`converter/youtube-toMp3.py`** — populate `playlist_urls` list with YouTube playlist URLs

Output files land in `<BASE_PATH>/music/`, logs in `<BASE_PATH>/download_log.txt`, and the skip-archive (already-downloaded IDs) in `<BASE_PATH>/downloaded.txt`.

## yt_dlp Options

The downloader uses Chrome cookies (`cookiesfrombrowser: ("chrome",)`) to bypass age restrictions — Chrome must be installed and logged in. Change to `"firefox"` or `"edge"` if needed.

The `download_archive` file prevents re-downloading tracks across runs. Delete `downloaded.txt` to force a full re-download.
