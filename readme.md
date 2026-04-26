# How to use this RAG AI Teaching Assistant on your own data
## step-1 collect your videos
move your all video to videos  folder

## step-2 convert videos into mp3
convert all the video by running to video_to_mp3 

## step-3 convert mp3 to json
convert all the mp3 files to json by running mp3_to_json

## convert json file to vectors
use the file preprocess_json to convert the json files to a data frame with embeddings and save it as a joblib pickle

## step-5  prompt  generation and feeding to llm
 read the joblib file and load it into the  memory.then create a relevant prompt as per the user query and feed it to the llm