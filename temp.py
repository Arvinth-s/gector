from distutils.file_util import write_file
from datasets import load_dataset
from tqdm import tqdm
import numpy as np
import re

Tamil_Dataset = {
    'dataset_name': 'oscar',
    'dataset_subset': 'unshuffled_deduplicated_ta',
    'text_label' : 'text',
    'test_sentence': "பொழுது சாய்ந்து வெகு நேரமாகிவிட்டது 😁 ?",
}
curDataset = Tamil_Dataset
train_dataset = load_dataset(curDataset["dataset_name"] , curDataset["dataset_subset"], split='train[:1]')

import stanza
# stanza.download('ta')       # This downloads the English models for the neural pipeline
nlp = stanza.Pipeline(lang='ta', processors='tokenize,mwt,pos') # This sets up a default neural pipeline in English
write_file = open('temp.txt', 'w')
for sentence in train_dataset:
    print('sentence:', sentence['text'])
    doc = nlp(sentence['text']) 
    for sent in doc.sentences:
        for word in sent.words:
            if(word.pos=='VERB'):
                # print(f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}')
                i = word.text
                y= i
                if re.findall("ஂதாள்$", i): y=re.sub("ஂதாள்$", "ிருபஂபாள்", i)
                elif re.findall("ஂதான்$", i): y=re.sub("ஂதான்$", "ிருபஂபாள்", i)
                elif re.findall("ஂபாள்$", i): y=re.sub("ிருபஂபாள்$", "ஂதான்", i)
                elif re.findall("ஂபான்$", i): y=re.sub("ிருபஂபான்$", "ஂதான்", i)
                if re.findall("ாள்$", i): y=re.sub("ாள்$", "து", i)
                if(i != y):
                    print('i', i, ' y', y)
                elif re.findall("ான்$", i): y=re.sub("ான்$", "து", i)
                elif re.findall("ன்$", i): y=re.sub("ன்$", "து", i)
                elif re.findall("ள்$", i): y=re.sub("ள்$", "து", i)
                if(i != y):
                    print('i', i, ' y', y)
                if re.findall("ள்$", i): y=re.sub("ள்$", "ரஂ௧ளஂ", i)
                else: y=re.sub("ன்$", "ரஂ௧ளஂ", i)
                if(i != y):
                    print('i', i, ' y', y)
                
    # doc.sentences[0].print_dependencies()
    # print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
    # write_file.write(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')