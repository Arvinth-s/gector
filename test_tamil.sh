python predict.py \
--model_path models/best.th \
--input_file 'dump/input.txt' \
--output_file 'dump/output.txt' \
--transformer_model bert \
--vocab_path 'models/vocabulary'
echo 'Output generated'