# YT2Sum
Simple YouTube to text summary converter
This code uses the pytube library to download an audio version of a YouTube video specified by a link inputted by the user. The audio file is then transcribed using the whisper library and the transcript is passed to the Chatbot class from the revChatGPT package. The chatbot summarizes the transcript and saves the summary to a file called response.txt.

## Dependencies
* pytube
* revChatGPT
* whisper

## Usage
1. Run the code with the command python3 <filename>.py
2. Input the link of the YouTube video you want to summarize when prompted
3. The audio file will be downloaded and transcribed
4. The transcript will be sent to the Chatbot class for summarization
5. The summary will be saved to a file called response.txt in the same directory as the code

## Note 
You must provide your own session_token for the Chatbot class in the code.
