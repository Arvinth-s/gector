echo 'Training Tamil'

rm -r models
mkdir models

python train.py \
--train_set 'dump/tamil/train/data/tamil_train.txt' \
--dev_set 'dump/tamil/dev/data/tamil_train.txt' \
--model_dir ./models \
--updates_per_epoch 1000 \
--transformer_model bert \
# --n_epoch 20 \ 


echo 'Training completed'