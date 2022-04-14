clear

rm ./dump/tamil -r
mkdir -p ./dump/tamil/train/
mkdir -p ./dump/tamil/dev/


python error_creator.py --savedir './dump/tamil/' --n 1

errant_parallel -orig './dump/tamil/train/original.txt' -cor './dump/tamil/train/corrupted.txt'  -out './dump/tamil/train/m2check.txt'
errant_parallel -orig './dump/tamil/dev/original.txt' -cor './dump/tamil/dev/corrupted.txt'  -out './dump/tamil/dev/m2check.txt'

cd errorify
python ./error.py '../dump/tamil/train/m2check.txt' ../dump/tamil/train
python ./error.py '../dump/tamil/dev/m2check.txt' ../dump/tamil/dev
cd ..

mkdir ./dump/tamil/train/data
mkdir ./dump/tamil/dev/data
python ./utils/preprocess_data.py -s 'dump/tamil/train/incorr_sentences.txt' -t 'dump/tamil/train/corr_sentences.txt' -o 'dump/tamil/train/data/tamil_train.txt'
python ./utils/preprocess_data.py -s 'dump/tamil/dev/incorr_sentences.txt' -t 'dump/tamil/dev/corr_sentences.txt' -o 'dump/tamil/dev/data/tamil_train.txt'

echo 'Training Tamil'

python train.py \
--train_set 'dump/tamil/train/data/tamil_train.txt' \
--dev_set 'dump/tamil/dev/data/tamil_train.txt' \
--model_dir ./models2 \
--transformer_mode roberta \
--updates_per_epoch 10

echo 'Training completed'
