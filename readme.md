# STEP 1:- collect your video 
move all your video files to the video folder

# STEP 2:- convert to mp3
convert the all video files to mp3 by running video_to_mp3

# STEP3:- convert mp3 to json
convert the all mp3 files to json by running mp3_to_json

# STEP 4:- convert json file to vectors
use the file preprocess_json to convert the json files to a dataframe with embedding and save it as joblib pickle

# step 5:- propt generation and feeding to LLM
read the joblin file and load it into the memory. then create a relevant prompt as per the user query and feed it to the LLM
