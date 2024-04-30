import whisper

model = whisper.load_model("base")
#print home directory
import os
print(os.path.expanduser("~"))
dir=os.path.expanduser("~")+"/work/"
print(dir)
file=dir+'pr.mp3'
result = model.transcribe(file)
#result = model.transcribe("pr.mp3")
#save dict to file
import json
with open('pr.json', 'w') as f:
    json.dump(result, f)
#load dict from file
# save text to file
with open('pr.txt', 'w') as f:
    f.write(result["text"])
    
        

print(result["text"])