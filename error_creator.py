import numpy as np
import re
from datasets import load_dataset
import os
from tqdm import tqdm
import argparse


fixed_random_words='''தீவினுக்கோர் பாலம் அமைப்போம் -மகாகவி Welcome to delegates of Bharathi International நீல வண்ணத்தில் எழுத்துக்கள் வெள்ளைத் ...
தென்னல் காற்று வீசுவது நின்று சுமார் ஒரு மாதகாலமாயிற்று. முன்னாள் ஜனாதிபதி மஹிந்த ராஜபக்ஷவினால் முன்னெடுக்கப்பட்ட போராட்டம் உட்பட வேலைநிறுத்த போராட்டங்களுக்கான நிதி அனுசரணையை சீனாவே வழங்கி நாட்டையும் அரசாங்கத்தையும் நெருக்கடிக்குள்ளாக்க முயல்கிறது என சமூக நலன்புரி பிரதி அமைச்சர் ரஞ்சன் ராமநாயக்க தெரிவித்தார்.
நேற்று முன்னாள் ஜனாதிபதி மஹிந்த ராஜபக்ஷவின் தலைமையில் போராட்டம் முன்னெடுக்கப்பட்ட போராட்டத்தின் பின்னணியில் சீனாவே உள்ளது
போராட்டங்கள் நடத்தும் அளவுக்கு மஹிந்த அணியினருக்கு எங்கிருந்து பணம் வருகின்றது
ஆகவே மஹிந்த அணியினர் பேரணிக்கும் நாட்டில் நடத்தப்படும் வேலைநிறுத்த போராட்டங்களுக்கும் சீனாவே நிதி வழங்குகின்றது.
இலங்கையில் நெருக்கடியான நிலைமையை ஏற்படுத்தவே சீனா இவ்வாறு செயற்பட்டு வருகின்றது
சீனா விவகாரத்தில் கழுத்து நசுக்கப்பட்ட நிலைமையிலேயே நாம் உள்ளோம்
ஆகவே எமது நாட்டை நெருக்கடிக்கு உள்ளாக்க வேண்டாம் என சீனாவிடம் நான் தலைகுனிந்து வேண்டுகின்றேன்.
அத்துடன் பொன்சேகாவுக்கு அருகில் இருந்த பாதாள கோஷ்டி ஒருவரை கைது செய்ததை போன்று ஏனைய அமைச்சர்களின் பதாள கோஷ்டியினரை கைது செய்ய வேண்டும் என்றும் அவர் குறிப்பிட்டார்.
திருமதி'''
fixed_random_words=fixed_random_words.split(' ')
 
parser = argparse.ArgumentParser()
 
parser.add_argument("-sd", "--savedir", help = "dataset directory", default='dump/tamil2/')
parser.add_argument("-n", "--ndata", help = "size of dataset", default=10, type=int)
# 0 for tamil 1 for english
parser.add_argument("-lang", "--language", help = "Choose the dataset language", default=0, type=int, choices=[0, 1])
 
args = parser.parse_args()
 

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

def corrupt_gender(data, corrupt_prob_percent=10):
  output_data=""
  for i in data.split(" "):
    x=np.random.randint(100, size=1)[0]
    y=i
    if x <= corrupt_prob_percent:
      if re.findall("ள்$", i): y=re.sub("ள்$", "ன்", i)
      else: y=re.sub("ன்$", "ள்", i)
    output_data+=y+" "
  return(output_data)

# def corrupt_tense(data):
#   output_data=""
#   for i in data.split(" "):
#     x=np.random.randint(2, size=1)[0]
#     y=i
#     if x==0:
#       if re.findall("ஂதாள்$", i): y=re.sub("ஂதாள்$", "ிருபஂபாள்", i)
#       elif re.findall("ஂதான்$", i): y=re.sub("ஂதான்$", "ிருபஂபாள்", i)
#       elif re.findall("ஂபாள்$", i): y=re.sub("ிருபஂபாள்$", "ஂதான்", i)
#       elif re.findall("ஂபான்$", i): y=re.sub("ிருபஂபான்$", "ஂதான்", i)
#     output_data+=y+" "
#   return(output_data)

def corrupt_pluarlity(data, corrupt_prob_percent=10):
  output_data=""
  for i in data.split(" "):
    x=np.random.randint(100, size=1)[0]
    y=i
    if x<=corrupt_prob_percent:
      if re.findall("ள்$", i): y=re.sub("ள்$", "ரஂ௧ளஂ", i)
      else: y=re.sub("ன்$", "ரஂ௧ளஂ", i)
    output_data+=y+" "
  return(output_data)

def corrupt_thinai(data, corrupt_prob_percent=10):
  output_data=""
  for i in data.split(" "):
    x=np.random.randint(100, size=1)[0]+1
    y=i
    if(x <= corrupt_prob_percent):
      if re.findall("ாள்$", i): y=re.sub("ாள்$", "து", i)
      elif re.findall("ான்$", i): y=re.sub("ான்$", "து", i)
      elif re.findall("ன்$", i): y=re.sub("ன்$", "து", i)
      elif re.findall("ள்$", i): y=re.sub("ள்$", "து", i)
      # elif re.findall("து$", i): y=re.sub("து$", "ள்", i)
    output_data+=y+" "
  return(output_data)

def remove_random_chars(data, remove_prob_percent=10):
  output_data = ""
  for i in data:
    x=np.random.randint(100, size=1)[0]+1
    if(x > remove_prob_percent):
      output_data += i
  return output_data

def remove_random_words(data, remove_prob_percent=5):
  output_data=""
  for i in data.split(" "):
    x=np.random.randint(100, size=1)[0]+1
    if(x > remove_prob_percent):
      output_data += i + " "
  return(output_data)

def repeat_words(data, repeat_prob_percentage=5):
  output_data=""
  for i in data.split(" "):
    x=np.random.randint(100, size=1)[0]+1
    if(x <= repeat_prob_percentage):
      output_data += i + " "
    output_data+=i+" "
  return(output_data)

def add_random_words(data, random_words=fixed_random_words, add_prob_percentage=5):
  output_data=""
  n = len(random_words)
  if(n==0): return data
  for i in data.split(" "):
    x=np.random.randint(100, size=1)[0]+1
    idx=np.random.randint(n, size=1)[0]
    if(x <= add_prob_percentage):
      output_data += random_words[idx] + " "
    output_data+=i+" "
  return(output_data)

def merge_sentence(data, merge_prob_percent=10):
  output_data = ""
  for i in data:
    if(i == '.'):
      x=np.random.randint(100, size=1)[0]+1
      if(x > merge_prob_percent):
        output_data += " மற்றும்"
    return output_data

Tamil_Dataset = {
    'dataset_name': 'oscar',
    'dataset_subset': 'unshuffled_deduplicated_ta',
    'text_label' : 'text',
    'test_sentence': "பொழுது சாய்ந்து வெகு நேரமாகிவிட்டது 😁 ?",
}

English_Dataset = {
    'dataset_name': 'glue',
    'dataset_subset': 'cola',
    'text_label' : 'sentence', 
    'test_sentence': "Hello, y'all! How are you 😁 ?"
}


if(args.language==0):
  curDataset = Tamil_Dataset
else: 
  curDataset = English_Dataset

dataset_len = args.ndata


train_dataset = load_dataset(curDataset["dataset_name"] , curDataset["dataset_subset"], split='train[:100]')
test_dataset = load_dataset(curDataset["dataset_name"] , curDataset["dataset_subset"], split='train[100:]')
print(test_dataset)
# print(dataset[0][curDataset["text_label"]])



save_dir = args.savedir+'train/'

if(not os.path.isdir(save_dir)):
  os.makedirs(save_dir)

f_org = open(save_dir + 'original.txt', 'w')
f_cor = open(save_dir + 'corrupted.txt', 'w')
# dataset_len = len(dataset)

count = 0

for data in tqdm(train_dataset, total=dataset_len):
  count += 1
  if(count > dataset_len): break
  data = data[curDataset["text_label"]]
  data_original = list(data.split(". "))

  
  for d in data_original:
    if(d=='\n' or len(d)==0):continue
    d += "\n"
    f_org.write(d)


  # data=corrupt_gender(data)
  # data=corrupt_homophones(data)
  # data=remove_random_chars(data, 10)

  # data_corrupted = list(data.split(". "))

  data=remove_random_words(data, 10)
  data=add_random_words(data, fixed_random_words, 30)
  data=repeat_words(data, 30)
  data=merge_sentence(data, 30)
  data=corrupt_thinai(data, 30)
  data=corrupt_gender(data, 30)
  data=corrupt_homophones(data)
  data=remove_random_chars(data)
  data_corrupted = list(data.split(". "))

  for d in data_corrupted:
    if(d=='\n' or len(d)==0):continue
    d += "\n"
    f_cor.write(d)

f_org.close()
f_cor.close()

save_dir = args.savedir+'dev/'


f_org = open(save_dir + 'original.txt', 'w')
f_cor = open(save_dir + 'corrupted.txt', 'w')

count = 0

for data in tqdm(test_dataset, total=dataset_len):
  count += 1
  if(count > dataset_len): break
  data = data[curDataset["text_label"]]
  data_original = list(data.split(". "))
  # print('length of original data', len(data_original))
  
  for d in data_original:
    if(d=='\n' or len(d)==0):continue
    d += "\n"
    f_org.write(d)


  data=remove_random_words(data, 10)
  data=add_random_words(data, fixed_random_words, 30)
  data=repeat_words(data, 30)
  data=merge_sentence(data, 30)
  data=corrupt_thinai(data, 30)
  data=corrupt_gender(data, 30)
  data=corrupt_homophones(data)
  data=remove_random_chars(data)
  data_corrupted = list(data.split(". "))
  # print('length of corrupted data', len(data_corrupted))

  for d in data_corrupted:
    if(d=='\n' or len(d)==0):continue
    d += "\n"
    f_cor.write(d)

f_org.close()
f_cor.close()

'''
# print("--------------------------------- Corrupted Data ---------------------------------")
# print(data)
இருந்தாள்
மா
ாம
'''