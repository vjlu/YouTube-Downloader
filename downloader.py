import os
import sys
import yt_dlp

def progress_hook(d):
    """Callback hook to display real-time download progress."""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A').strip()
        speed = d.get('_speed_str', 'N/A').strip()
        eta = d.get('_eta_str', 'N/A').strip()
        print(f"\rDownloading: {percent} | Speed: {speed} | ETA: {eta}", end="", flush=True)
    elif d['status'] == 'finished':
        print("\nDownload finished! Post-processing...")

def get_available_resolutions(info_dict):
    """Extract and sort all unique available video resolutions."""
    formats = info_dict.get('formats', [])
    resolutions = set()
    
    for f in formats:
        # Check for video streams with valid height
        if f.get('vcodec') != 'none' and f.get('height'):
            resolutions.add(f['height'])
            
    # Sort resolutions from highest to lowest (e.g., 2160, 1440, 1080, 720)
    return sorted(list(resolutions), reverse=True)

def main():
    print("=" * 50)
    print("      CUSTOM YOUTUBE VIDEO & AUDIO DOWNLOADER     ")
    print("=" * 50)

    url = input("Enter YouTube Video URL: ").strip()
    if not url:
        print("Error: No URL provided.")
        return

    # Output directory
    output_dir = input("Enter download directory (press Enter for current folder): ").strip()
    if not output_dir:
        output_dir = "downloads"
    
    os.makedirs(output_dir, exist_ok=True)

    print("\nFetching video metadata... Please wait.")
    
    # Extract metadata without downloading
# Extract metadata without downloading (UPDATED)
    ydl_opts_info = {
        'quiet': True, 
        'no_warnings': True,
        'cookiefile': 'cookies.txt',  # Change 'chrome' to 'edge', 'firefox', or 'brave' if needed
        'extractor_args': {'youtube': ['player_client=default']}
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Unknown Title')
            duration = info.get('duration_string', 'N/A')
            print(f"\nTitle: {title}")
            print(f"Duration: {duration}")
    except Exception as e:
        print(f"\nFailed to fetch video details: {e}")
        return

    # Format selection menu
    print("\nSelect Download Format:")
    print(" [1] Video (MP4)")
    print(" [2] Audio (MP3)")
    print(" [3] Audio (M4A)")
    
    format_choice = input("Enter choice (1-3): ").strip()
    
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'quiet': True,
        'no_warnings': True,
        'cookiefile': 'cookies.txt',   # <--- ADD THIS LINE (Change to your actual browser)
        'extractor_args': {'youtube': ['player_client=default']}  # <--- ADD THIS LINE
    }

    if format_choice == '1':
        # Video (MP4) option
        resolutions = get_available_resolutions(info)
        
        print("\nAvailable Resolutions:")
        print(" [0] Best Available (Highest Quality)")
        for i, res in enumerate(resolutions, start=1):
            print(f" [{i}] {res}p")

        res_choice = input(f"Choose resolution (0-{len(resolutions)}): ").strip()

        if res_choice == '0' or not res_choice.isdigit() or int(res_choice) > len(resolutions):
            # Best video + best audio merged into MP4 container
            ydl_opts['format'] = 'bestvideo+bestaudio/best'
        else:
            selected_height = resolutions[int(res_choice) - 1]
            # Match selected resolution and merge with best audio
            ydl_opts['format'] = f'bestvideo[height<={selected_height}]+bestaudio/best[height<={selected_height}]'

        ydl_opts['merge_output_format'] = 'mp4'

    elif format_choice == '2':
        # Audio (MP3) option
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',  # 320 kbps high-quality audio
        }]

    elif format_choice == '3':
        # Audio (M4A) option
        ydl_opts['format'] = 'bestaudio[ext=m4a]/bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '0',   # Keep original AAC stream quality
        }]
    else:
        print("Invalid choice selected. Exiting.")
        return

    # Start the download
    print("\nStarting download...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\nSuccess! File saved to: {os.path.abspath(output_dir)}\n")
    except Exception as e:
        print(f"\nDownload error: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProcess cancelled by user.")
        sys.exit(0)