# 🎥 YouTube Video & Audio Downloader

<p align="center">
  <strong>A simple, powerful command-line YouTube downloader built with Python and yt-dlp.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/yt--dlp-powered-red?style=for-the-badge" alt="yt-dlp">
  <img src="https://img.shields.io/badge/MP4-Video-green?style=for-the-badge" alt="MP4">
  <img src="https://img.shields.io/badge/MP3%20%2F%20M4A-Audio-orange?style=for-the-badge" alt="Audio">
</p>

---

## ✨ Features

* 🎬 **Video downloads** in MP4
* 🎵 **MP3 audio extraction** at 320 kbps
* 🎧 **M4A audio downloads** while preserving the original AAC quality
* 📺 **Resolution selection** based on the formats available for the video
* ⚡ **Best available quality** option
* 📊 **Real-time download progress** with speed and ETA
* 🍪 **Cookie support** using a local `cookies.txt` file
* 📁 **Custom download directory**
* 🔎 **Video metadata preview** before downloading
* 🛠️ Powered by the reliable [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) engine
* 🐍 Lightweight Python script — no complicated GUI or setup

---

## 🖥️ How It Works

The workflow is intentionally simple:

```text
YouTube URL
     │
     ▼
Fetch video information
     │
     ▼
Choose format
 ┌───┼────────────┐
 ▼   ▼            ▼
MP4 MP3          M4A
 │
 ▼
Choose resolution
 │
 ▼
Download
 │
 ▼
Done! 🎉
```

---

# 🚀 Installation

## 1. Install Python

Make sure Python 3 is installed on your system.

You can check with:

```bash
python --version
```

or on Windows:

```powershell
py --version
```

---

## 2. Install yt-dlp

Install the required Python package:

```bash
pip install yt-dlp
```

---

## 3. Install FFmpeg

FFmpeg is required for operations such as:

* Merging separate video and audio streams
* Converting audio to MP3
* Processing downloaded media

Make sure `ffmpeg` is available in your system PATH, or place the FFmpeg executable where your system can access it.
(it is already bundled with script in "Releases" Section, so you don't need to do any of this if you Installed it from there)
You can verify the installation with:

```bash
ffmpeg -version
```

---

# 🍪 Cookie Setup

Some YouTube downloads may require an authenticated browser session.

This downloader supports a local `cookies.txt` file.

### Recommended setup

Install the Chrome extension:

**Get cookies.txt LOCALLY**

https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc

Then:

1. Open **YouTube** in Chrome.
2. Make sure you are logged into your account if necessary.
3. Click the **Get cookies.txt LOCALLY** extension.
4. Export the cookies.
5. Save the exported file as:

```text
cookies.txt
```

6. Place `cookies.txt` in the **same folder as `downloader.py`**.

Your folder should look like:

```text
youtube-downloader/
│
├── downloader.py
├── cookies.txt
└── ...
```


---

# ▶️ Usage

Once everything is installed, run:

```powershell
py downloader.py
```

You'll see:

```text
==================================================
      CUSTOM YOUTUBE VIDEO & AUDIO DOWNLOADER
==================================================

Enter YouTube Video URL:
```

### 1. Paste the URL

Paste the YouTube video URL and press Enter.

The program will retrieve the video's:

* Title
* Duration
* Available video resolutions

---

### 2. Choose your format

You'll be presented with:

```text
Select Download Format:
 [1] Video (MP4)
 [2] Audio (MP3)
 [3] Audio (M4A)
```

Choose the option you want.

---

### 3. Choose video resolution

For MP4 downloads, the available resolutions are detected automatically.

For example:

```text
Available Resolutions:
 [0] Best Available (Highest Quality)
 [1] 2160p
 [2] 1440p
 [3] 1080p
 [4] 720p
 [5] 480p
```

Select your preferred quality.

---

### 4. Download 🎉

The downloader displays real-time information:

```text
Downloading: 47.3% | Speed: 8.42MiB/s | ETA: 00:12
```

When finished:

```text
Download finished! Post-processing...

Success! File saved to: ...
```

---

# 📦 Output Formats

| Format | Description                                             |
| ------ | ------------------------------------------------------- |
| 🎬 MP4 | Video + audio merged into an MP4 file                   |
| 🎵 MP3 | Audio extracted and converted to 320 kbps MP3           |
| 🎧 M4A | Audio downloaded as M4A while preserving source quality |

The script uses `bestvideo+bestaudio` for high-quality video downloads and merges them into an MP4 container.

MP3 downloads use FFmpeg extraction with a preferred quality of 320 kbps, while M4A uses the original AAC stream when available.

---

# 📂 Download Location

By default, downloads are placed inside:

```text
downloads/
```

You can also specify a custom directory when the program starts.

Example:

```text
Enter download directory (press Enter for current folder):
D:\Videos
```

---

# 🛠️ Project Structure

```text
youtube-downloader/
│
├── downloader.py       # Main downloader
├── cookies.txt         # Local browser cookies (DO NOT COMMIT)
├── .gitignore          # Git ignored files
└── README.md           # Documentation
```

---

# 🔧 Technologies

This project is built with:

* **Python**
* **yt-dlp**
* **FFmpeg**

The downloader uses `yt_dlp.YoutubeDL` for metadata extraction and media downloading.

---

# ⚠️ Important

This project is intended for **personal and legitimate media downloading**.

Respect:

* YouTube's Terms of Service
* Copyright laws
* Content creators' rights
* The permissions associated with the content you download

Only download content that you have the right or permission to download.

---

# 🔐 Security

### Never upload your cookies.

Your `cookies.txt` may contain authentication/session information.


---

# 🐛 Troubleshooting

### `No module named 'yt_dlp'`

Install yt-dlp:

```bash
pip install yt-dlp
```

---

### FFmpeg errors

Make sure FFmpeg is installed and accessible:

```bash
ffmpeg -version
```

---

### Unable to retrieve video information

Check that:

* The URL is valid.
* Your internet connection is working.
* `cookies.txt` is present if authentication is required.
* yt-dlp is up to date.

Update yt-dlp:

```bash
pip install -U yt-dlp
```

---

# 🚧 Future Ideas

Some features that could be added in future versions:

* [ ] Playlist downloading
* [ ] YouTube Shorts support
* [ ] Custom audio quality selection
* [ ] Custom filename templates
* [ ] Thumbnail downloading
* [ ] Subtitle downloading
* [ ] Playlist progress tracking
* [ ] Configuration file
* [ ] Graphical user interface
* [ ] Automatic FFmpeg detection
* [ ] Cross-platform improvements

---

# ⭐ Support the Project

If you find this project useful, consider giving it a ⭐ on GitHub.

It helps the project get discovered and motivates further development.

---

## 📜 License

MIT License

---

<p align="center">
  Made with ❤️ and Python
</p>
