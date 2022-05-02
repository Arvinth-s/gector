start_time=$(date +%s.%3N)


python predict.py \
--model_path models2/model_state_epoch_2.th \
--input_file 'dump/input.txt' \
--output_file 'dump/output.txt' \
--transformer_model bert \
--vocab_path 'models/vocabulary'
echo 'Output generated'

end_time=$(date +%s.%3N)

elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo "Elapsed time: "  $elapsed