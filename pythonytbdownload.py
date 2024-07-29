import yt_dlp

# Ask for the link from the user
link = input("Enter the link of the YouTube video you want to download: ")

# Define the download options
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Download best available quality
    'outtmpl': '%(title)s.%(ext)s',        # Save the file with the title of the video
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the video
        ydl.download([link])
    print("Download completed!!")
except Exception as e:
    print(f"An error occurred: {e}")
