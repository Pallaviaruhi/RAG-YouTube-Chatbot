from youtube_transcript_api import YouTubeTranscriptApi
import re 

def get_video_id(url_or_id:str)->str:
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url_or_id)
    return match.group(1) if match else url_or_id

def fetch_transcript(video_url_or_id: str) -> str:
    video_id = get_video_id(video_url_or_id)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'hi'])
        text = " ".join([t['text'] for t in transcript])
        return text
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

if __name__ == "__main__":
    url = input("Enter YouTube URL or Video ID: ")
    content = fetch_transcript(url)
    print(content[:1000] if content else "No transcript found.")
