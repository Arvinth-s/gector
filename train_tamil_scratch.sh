clear

pip install -r requirements.txt

rm ./dump/tamil -r
mkdir -p ./dump/tamil/train/
mkdir -p ./dump/tamil/dev/

clear

echo "installed requirements"


python error_creator.py --savedir './dump/tamil/' --n 100 --lang 0


mkdir ./dump/tamil/train/data
mkdir ./dump/tamil/dev/data
python ./utils/preprocess_data.py -s 'dump/tamil/train/corrupted.txt' -t 'dump/tamil/train/original.txt' -o 'dump/tamil/train/data/tamil_train.txt'
python ./utils/preprocess_data.py -s 'dump/tamil/dev/corrupted.txt' -t 'dump/tamil/dev/original.txt' -o 'dump/tamil/dev/data/tamil_train.txt'

echo 'Training Tamil'

rm -r models
mkdir models

python train.py \
--train_set 'dump/tamil/train/data/tamil_train.txt' \
--dev_set 'dump/tamil/dev/data/tamil_train.txt' \
--model_dir ./models \
--updates_per_epoch 10000 \
--transformer_model bert \
# --n_epoch 20 \ 

echo 'Training completed'

python predict.py \
--model_path models/best.th \
--input_file 'dump/input.txt' \
--output_file 'dump/output.txt' \
--transformer_model bert \
--vocab_path 'models/vocabulary'
echo 'Output generated'