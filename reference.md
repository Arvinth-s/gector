### OM NAMO NARAYANA


<hr/>
<br/>

## setup script
```
conda activate gector
pip install -r requirements.txt
curl https://www.cl.cam.ac.uk/research/nl/bea2019st/data/fce_v2.1.bea19.tar.gz | tar -xz
```

## Preprocess script
```
python utils/preprocess_data.py -s 'fce/m2/fce.train.gold.bea19.m2' -t 'fce/m2/fce.train.gold.bea19.m2' -o 'fce/m2/fce.train_preprocessed.gold.bea19.m2'

python utils/preprocess_data.py -s 'fce/m2/fce.dev.gold.bea19.m2' -t 'fce/m2/fce.dev.gold.bea19.m2' -o 'fce/m2/fce.dev_preprocessed.gold.bea19.m2'

python utils/preprocess_data.py -s 'fce/m2/fce.test.gold.bea19.m2' -t 'fce/m2/fce.test.gold.bea19.m2' -o 'fce/m2/fce.test_preprocessed.gold.bea19.m2'
```

## Testing script
Create a input.txt file in dump/
```
cd MODEL_DIR && wget https://grammarly-nlp-data-public.s3.amazonaws.com/gector/roberta_1_gectorv2.th && cd ..

python predict.py --model_path MODEL_DIR/roberta_1_gectorv2.th --input_file 'dump/input.txt' --output_file 'dump/out.txt' --special_tokens_fix 1 --max_len 150 --transformer_model roberta --vocab_path data/output_vocabulary
```
