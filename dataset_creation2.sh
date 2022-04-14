clear

rm ./dump/tamil2 -r
mkdir -p ./dump/tamil2/train/
mkdir -p ./dump/tamil2/dev/


python error_creator2.py --savedir './dump/tamil2/' --n 1

errant_parallel -orig './dump/tamil2/train/original.txt' -cor './dump/tamil2/train/corrupted.txt'  -out './dump/tamil2/train/m2check.txt'
errant_parallel -orig './dump/tamil2/dev/original.txt' -cor './dump/tamil2/dev/corrupted.txt'  -out './dump/tamil2/dev/m2check.txt'

cd errorify
python ./error.py '../dump/tamil2/train/m2check.txt' ../dump/tamil2/train
python ./error.py '../dump/tamil2/dev/m2check.txt' ../dump/tamil2/dev
cd ..

mkdir ./dump/tamil2/train/data
mkdir ./dump/tamil2/dev/data
python ./utils/preprocess_data.py -s 'dump/tamil2/train/incorr_sentences.txt' -t 'dump/tamil2/train/corr_sentences.txt' -o 'dump/tamil2/train/data/tamil_train.txt'
python ./utils/preprocess_data.py -s 'dump/tamil2/dev/incorr_sentences.txt' -t 'dump/tamil2/dev/corr_sentences.txt' -o 'dump/tamil2/dev/data/tamil_train.txt'

echo 'Training Tamil'

python train.py \
--train_set 'dump/tamil2/train/data/tamil_train.txt' \
--dev_set 'dump/tamil2/dev/data/tamil_train.txt' \
--model_dir ./models2 \
--transformer_mode roberta \
--updates_per_epoch 10

echo 'Training completed'
