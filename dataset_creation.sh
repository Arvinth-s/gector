clear

rm ./dump/tamil -r
mkdir ./dump/tamil/


python error_creator.py

errant_parallel -orig './dump/tamil/original.txt' -cor './dump/tamil/corrupted.txt'  -out './dump/tamil/m2check.txt'

cd errorify
python ./error.py '../dump/tamil/m2check.txt' ../dump/tamil/
cd ..

mkdir ./dump/tamil/data
python ./utils/preprocess_data.py -s 'dump/tamil/incorr_sentences.txt' -t 'dump/tamil/corr_sentences.txt' -o 'dump/data/tamil_train.txt'

# echo 'Training with updated_per_epoch set to 1'
# python train.py \
# --train_set 'dump/data/tamil_train.txt' \
# --dev_set 'dump/data/tamil_train.txt' \
# --model_dir ./models \
# --transformer_mode roberta \
# --updates_per_epoch 1
# echo 'Training completed'
