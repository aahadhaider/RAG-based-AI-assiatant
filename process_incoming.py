import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import requests
import os
import numpy as np
import joblib
from openai import OpenAI
from config import api_key

client=OpenAI(api_key=api_key)

def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed", json={
        "model":"bge-m3",
        "input":text_list
    })
    embedding= r.json()["embeddings"]
    return embedding

def inference(prompt):
    r=requests.post("http://localhost:11434/api/generate", json={
        # "model":"deepseek-r1:latest",
        "model": "llama3.2",
        "prompt": prompt,
        "stream":False
    })

    response=r.json()
    print(response)
    return response

def inference_openai(prompt):
    response = client.responses.create(
    model="gpt-5",
    input=prompt
)

    return response.output_text


df=joblib.load("embeddings.joblib")

incoming_query=input("ask a question:")
question_embedding=create_embedding([incoming_query])[0]
print(question_embedding)

# a = create_embedding("aahad will go for an interview on monday,i am too bad in communication skills")
# print(a)
# print(df["embedding"].values)
# print(df["embedding"].shape)

similarities=cosine_similarity (np.vstack(df["embedding"].values),[question_embedding]).flatten()
#print(similarities)
top_result=5
max_index=similarities.argsort()[::-1][0:top_result]#top 3 indiceswher
#print(max_index)
new_df=df.loc[max_index]
#print(new_df[["number","title","chunk_id","text"]])

prompt=f'''i am teaching the web development course  here are video chunk containing video title,video number,start time in second,end time in setting,the text at that time stamp:

{new_df[["number","title","start","end","text"]].to_json(orient="records")}
-------------------------

"{incoming_query}"
user asked this queston related to video chunk,you have to answe where amd how much content is taught where(in which video at what timestamp) and guide user to go that particular video.if user ask unrelated question,tell him that you can only answer question related to the course'''

with open("prompt.txt","w")as f:
    f.write(prompt)

# response=inference(prompt)["response"]
# print(response)

response=inference_openai(prompt)

with open("response.txt","w")as f:
    f.write(response)

# for index , item in new_df.iterrows():
#     print(index,item["title"],item["number"],item["text"])