start_time=$(date +%s.%3N)


model_path_arg=${1:-models/bert/best.th}
input_file_arg=${2:-dump/input.txt}

python predict.py \
--model_path $model_path_arg \
--input_file $input_file_arg \
--output_file 'dump/output.txt' \
--transformer_model xlm \
--vocab_path 'models/xlm/vocabulary'
echo 'Output generated'

end_time=$(date +%s.%3N)

elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo "Elapsed time: "  $elapsed
./telegram-send.sh "prediction-completed"