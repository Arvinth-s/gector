clear

rm ./dump/tamil -r
mkdir -p ./dump/tamil/train/
mkdir -p ./dump/tamil/dev/


python error_creator.py --savedir './dump/tamil/' --n 100 --lang 0

# errant_parallel -orig './dump/tamil/train/original.txt' -cor './dump/tamil/train/corrupted.txt'  -out './dump/tamil/train/m2check.txt'
# errant_parallel -orig './dump/tamil/dev/original.txt' -cor './dump/tamil/dev/corrupted.txt'  -out './dump/tamil/dev/m2check.txt'

# cd errorify
# python ./error.py '../dump/tamil/train/m2check.txt' ../dump/tamil/train
# python ./error.py '../dump/tamil/dev/m2check.txt' ../dump/tamil/dev
# cd ..

mkdir ./dump/tamil/train/data
mkdir ./dump/tamil/dev/data
python ./utils/preprocess_data.py -s 'dump/tamil/train/corrupted.txt' -t 'dump/tamil/train/original.txt' -o 'dump/tamil/train/data/tamil_train.txt'
python ./utils/preprocess_data.py -s 'dump/tamil/dev/corrupted.txt' -t 'dump/tamil/dev/original.txt' -o 'dump/tamil/dev/data/tamil_train.txt'

echo "data creation completed."
./telegram-send.sh "data-creation-completed"

# echo 'Training Tamil'

# python train.py \
# --train_set 'dump/tamil/train/data/tamil_train.txt' \
# --dev_set 'dump/tamil/dev/data/tamil_train.txt' \
# --model_dir ./models\
# --transformer_model xlm \
# --updates_per_epoch 1000 \
# -- n_epoch: 20 \ 


# --cold_steps_count: 2  \
# --accumulation_size: 4  \ 
# --tn_prob: 0  
# --tp_prob: 1  
# --pretrain: '' 

# --tune_bert: 1  \ 
# --skip_correct: 1 \  
# --skip_complex: 0   \ 
# --max_len: 50  \ 
# --batch_size: 8 \  
# --tag_strategy: keep_one \ 
# --cold_steps_count: 0  \
# --cold_lr: 1e-3  \
# --lr: 1e-5  \
# --predictor_dropout: 0.0  \
# --lowercase_tokens: 0  \
# --pieces_per_token: 5  \
# --vocab_path: ''  \
# --label_smoothing: 0.0 \
# --patience: 0  \

# echo 'Training completed'
