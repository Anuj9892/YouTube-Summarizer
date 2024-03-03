from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

try:
    # Get the YouTube video URL from the user
    
    youtube_video = input("Enter the URL: ")
    video_id = youtube_video.split("=")[1]

    # Get the transcript of the YouTube video
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Extract text from the transcript
    result = " ".join([i["text"] for i in transcript])

    # Initialize the summarizer pipeline
    summarizer = pipeline("summarization")

    # Split the text into chunks and summarize each chunk
    num_iters = int(len(result) / 1000)
    summarizer_text = []

    for i in range(0, num_iters + 1, 1):
        start = i * 1000
        end = (i + 1) * 1000
        chunk = result[start:end]
        out = summarizer(chunk)
        out = out[0]
        out = out["summary_text"]
        summarizer_text.append(out)

    print(summarizer_text)

except Exception as e:
    print(f"An error occurred: {e}")