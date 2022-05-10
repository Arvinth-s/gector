conda activate gector

echo 'Training Tamil'

# rm -r models
# mkdir models

start_time=$(date +%s.%3N)

model_dir_arg=${1:-models/xlm}
updates_per_epoch_arg=${2:-5000}
pretrain_folder_arg=${3:-models/xlm/}
pretrain_arg=${4:-best}

echo "parameters: 
model_dir ${model_dir_arg}
pretrain_folder ${pretrain_folder_arg} 
pretrain_model ${pretrain_arg}
updates_per_epoch ${updates_per_epoch_arg}"  

python train.py \
--train_set 'dump/tamil/train/data/tamil_train.txt' \
--dev_set 'dump/tamil/dev/data/tamil_train.txt' \
--model_dir $model_dir_arg \
--updates_per_epoch $updates_per_epoch_arg \
--transformer_model xlm \
--vocab_path $pretrain_folder_arg/vocabulary \
--pretrain_folder $pretrain_folder_arg \
--pretrain $pretrain_arg
# --n_epoch 20 \ 

end_time=$(date +%s.%3N)

elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo "Elapsed time: "  $elapsed

echo 'Training-completed'
./telegram-send.sh "Training-completed"

./telegram-send.sh "Stoping-instance"
./stop_instance.sh
