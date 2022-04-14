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
python utils/preprocess_data.py -s 'fce/m2/fce.train.gold.bea19.m2' -t 'fce/m2/fce.train.gold.bea19.m2' -o 'fce/m2/fce.train_preprocessed.gold.bea19.txt'

python utils/preprocess_data.py -s 'fce/m2/fce.dev.gold.bea19.m2' -t 'fce/m2/fce.dev.gold.bea19.m2' -o 'fce/m2/fce.dev_preprocessed.gold.bea19.txt'

python utils/preprocess_data.py -s 'fce/m2/fce.test.gold.bea19.m2' -t 'fce/m2/fce.test.gold.bea19.m2' -o 'fce/m2/fce.test_preprocessed.gold.bea19.txt'
```

## Training script
```
python train.py --train_set 'fce/m2/fce.train_preprocessed.gold.bea19.txt' --dev_set 'fce/m2/fce.dev_preprocessed.gold.bea19.txt' --vocab_path ./data/output_vocabulary/ --model_dir ./models --transformer_mode roberta
```

## Testing script
Create a input.txt file in dump/
```
cd MODEL_DIR && wget https://grammarly-nlp-data-public.s3.amazonaws.com/gector/roberta_1_gectorv2.th && cd ..

python predict.py --model_path MODEL_DIR/roberta_1_gectorv2.th --input_file 'dump/input.txt' --output_file 'dump/out.txt' --special_tokens_fix 1 --max_len 150 --transformer_model roberta --vocab_path data/output_vocabulary
```

## Useful issues
[dataset](https://github.com/grammarly/gector/issues/138)

[training_frozen](https://github.com/grammarly/gector/issues/58)

[training_code](https://github.com/grammarly/gector/issues/11)

[training_frozen_tqdm](https://github.com/grammarly/gector/issues/87)

[training_fronzen](https://github.com/grammarly/gector/issues/77)

[download_zip_repo](https://stackoverflow.com/questions/16261100/cant-download-github-project-with-curl-command)

[chiense_gector](https://github.com/grammarly/gector/issues/94)

## repo dependencies
[errant](https://github.com/chrisjbryant/errant)

[PIE](https://github.com/awasthiabhijeet/PIE/tree/master/errorify)