python predict.py \
--model_path models2/best.th \
--input_file 'dump/input.txt' \
--output_file 'dump/output.txt' \
--special_tokens_fix 1 \
--max_len 50 \
--transformer_model roberta \
--vocab_path 'models2/vocabulary'
# --vocab_path 'data/output_vocabulary'
echo 'Output generated'