# How to use this RAG based AI assistant on your own data?
## Step1 :  Collect your vedios.
Move all your vedio file to the vedios folder.

## Step2 : Convert to mp3.
 Convert all the vedio files to mp3 by running vedio_to_mp3

## Step3 : Convert mp3 to json.
 Convert all the mp3 files to json by running mp3_to_json.

## Step4 : Convert the json files to vector.
 Use the file preprocess json.py to convert all the json files into a data frame with Embeddings and save it as a joblib pickle

## Step5 : Promt generation and feeding it lo llm.
Read thge joblib file and load it into the memory.Then create a relevent promt as per the user query and feed it to LLM.
# RAG-BASE-AI-PROJECT
# RAG-BASE-AI-PROJECT
