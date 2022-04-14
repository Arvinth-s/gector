echo 'Training Tamil'

python train.py \
--train_set 'dump/tamil/data/tamil_train.txt' \
--dev_set 'dump/tamil/data/tamil_train.txt' \
--model_dir ./models \
--transformer_mode roberta \
--updates_per_epoch 1
echo 'Training completed'