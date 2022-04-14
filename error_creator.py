import numpy as np
import re
from datasets import load_dataset
import os
from tqdm import tqdm

def corrupt_homophones(data):
  output_data=""
  for i in data:
    x=np.random.randint(5, size=1)[0]

    if i=="ல":output_data += ["ள", "ழ", "ல", "ல", "ல"][x]
      
    elif i=="ள":output_data += ["ல", "ழ", "ள", "ள", "ள"][x]

    elif i=="ழ":output_data += ["ல", "ள", "ழ", "ழ", "ழ"][x]

    elif i=="ந":output_data += ["ண", "ன", "ந", "ந", "ந"][x]

    elif i=="ன":output_data += ["ண", "ந", "ன", "ன", "ன"][x]

    elif i=="ண":output_data += ["ன", "ந", "ண", "ண", "ண"][x]

    else: output_data+=i

  return(output_data)

def corrupt_gender(data):
  output_data=""
  for i in data.split():
    x=np.random.randint(2, size=1)[0]
    y=i
    if x==0:
      if re.findall("ள்$", i): y=re.sub("ள்$", "ன்", i)
      else: y=re.sub("ன்$", "ள்", i)
    output_data+=y+" "
  return(output_data)

Tamil_Dataset = {
    'dataset_name': 'oscar',
    'dataset_subset': 'unshuffled_deduplicated_ta',
    'text_label' : 'text',
    'test_sentence': "பொழுது சாய்ந்து வெகு நேரமாகிவிட்டது 😁 ?",
}

curDataset =Tamil_Dataset

dataset = load_dataset(curDataset["dataset_name"] , curDataset["dataset_subset"], split='train')
# print(dataset[0][curDataset["text_label"]])

save_dir = './dump/tamil/'

if(not os.path.isdir(save_dir)):
  os.makedirs(save_dir)

f_org = open(save_dir + 'original.txt', 'a')
f_cor = open(save_dir + 'corrupted.txt', 'a')
# dataset_len = len(dataset)
dataset_len = 50

count = 0

for data in tqdm(dataset, total=dataset_len):
  count += 1
  if(count > dataset_len): break
  data = data[curDataset["text_label"]]
  data_original = list(data.split(". "))

  
  for d in data_original:
    if(d=='\n' or len(d)==0):continue
    d += "\n"
    f_org.write(d)


  data=corrupt_gender(data)
  data=corrupt_homophones(data)

  data_corrupted = list(data.split(". "))

  for d in data_corrupted:
    if(d=='\n' or len(d)==0):continue
    d += "\n"
    f_cor.write(d)

f_org.close()
f_cor.close()


# print("--------------------------------- Corrupted Data ---------------------------------")
# print(data)
