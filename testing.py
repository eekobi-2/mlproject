import os
import pandas 
from src.utils import load_object
model_path=os.path.join("artifacts","model.pkl")

model=load_object(file_path=model_path)
            
data = [ "female", "group C","associate's degree","standard","none",91,86,84]
df = pandas.DataFrame(data)
 
        
preds=model.predict(df)

print(preds)