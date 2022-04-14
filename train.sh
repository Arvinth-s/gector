#!/bin/sh
conda activate gector

clear

# rm fce -r
# curl https://www.cl.cam.ac.uk/research/nl/bea2019st/data/fce_v2.1.bea19.tar.gz | tar -xz

mkdir ./dump/train
mkdir ./dump/dev
mkdir ./dump/test

cd errorify
python ./error.py '../fce/m2/fce.dev.gold.bea19.m2' ../dump/dev
python ./error.py '../fce/m2/fce.train.gold.bea19.m2' ../dump/train
python ./error.py '../fce/m2/fce.test.gold.bea19.m2' ../dump/test

cd ..
python ./utils/preprocess_data.py -s 'dump/train/incorr_sentences.txt' -t 'dump/train/corr_sentences.txt' -o 'dump/data/train.txt'

python ./utils/preprocess_data.py -s 'dump/dev/incorr_sentences.txt' -t 'dump/dev/corr_sentences.txt' -o 'dump/data/dev.txt'

python ./utils/preprocess_data.py -s 'dump/test/incorr_sentences.txt' -t 'dump/test/corr_sentences.txt' -o 'dump/data/test.txt'

# echo 'Training with updated_per_epoch set to 1'
echo 'Training...'
python train.py \
--train_set 'dump/data/train.txt' \
--dev_set 'dump/data/dev.txt' \
--vocab_path ./data/output_vocabulary/ \
--model_dir ./models_13_4 \
--transformer_mode roberta \
--updates_per_epoch 100
echo 'Training completed'

# echo 'Testing with custom input'
echo 'Testing...'
python predict.py \
--model_path models/best.th \
--input_file 'dump/input.txt' \
--output_file 'dump/output.txt' \
--special_tokens_fix 1 \
--max_len 150 \
--transformer_model roberta \
--vocab_path data/output_vocabulary
echo 'Output generated'