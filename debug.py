import os
from allennlp.data.vocabulary import DEFAULT_OOV_TOKEN, DEFAULT_PADDING_TOKEN
from allennlp.data.vocabulary import Vocabulary

from gector.datareader import Seq2LabelsDatasetReader
from gector.tokenizer_indexer import PretrainedBertIndexer


def get_token_indexers(model_name, max_pieces_per_token=5, lowercase_tokens=True, special_tokens_fix=0):
    bert_token_indexer = PretrainedBertIndexer(
        pretrained_model=model_name,
        max_pieces_per_token=max_pieces_per_token,
        do_lowercase=lowercase_tokens,
        special_tokens_fix=special_tokens_fix
    )
    return {'bert': bert_token_indexer}



def get_data_reader(model_name, max_len, skip_correct=False, skip_complex=0,
                    test_mode=False, tag_strategy="keep_one",
                    broken_dot_strategy="keep", lowercase_tokens=True,
                    max_pieces_per_token=3, tn_prob=0, tp_prob=1, special_tokens_fix=0,):
    token_indexers = get_token_indexers(model_name,
                                        max_pieces_per_token=max_pieces_per_token,
                                        lowercase_tokens=lowercase_tokens,
                                        special_tokens_fix=special_tokens_fix
                                        )
    reader = Seq2LabelsDatasetReader(token_indexers=token_indexers,
                                     max_len=max_len,
                                     skip_correct=skip_correct,
                                     skip_complex=skip_complex,
                                     test_mode=test_mode,
                                     tag_strategy=tag_strategy,
                                     broken_dot_strategy=broken_dot_strategy,
                                     lazy=True,
                                     tn_prob=tn_prob,
                                     tp_prob=tp_prob)
    return reader




train_set = 'dump/tamil/train/data/tamil_train.txt'

DEFAULT_NON_PADDED_NAMESPACES = ("*tags", "*labels")
DEFAULT_PADDING_TOKEN = "@@PADDING@@"
DEFAULT_OOV_TOKEN = "@@UNKNOWN@@"
NAMESPACE_PADDING_FILE = 'non_padded_namespaces.txt'

default_tokens = [DEFAULT_OOV_TOKEN, DEFAULT_PADDING_TOKEN]
namespaces = ['labels', 'd_tags']
tokens_to_add = {x: default_tokens for x in namespaces}


target_vocab_size = 1000


weights_name = 'xlm-roberta-base'
# read datasets

max_len = 50
skip_correct = 1
skip_complex = 0
tag_strategy = 'keep_one'
lowercase_tokens = 0
pieces_per_token = 5
tn_prob = 0
tp_prob = 1
special_tokens_fix = 1

reader = get_data_reader(weights_name, max_len, skip_correct=bool(skip_correct),
                             skip_complex=skip_complex,
                             test_mode=False,
                             tag_strategy=tag_strategy,
                             lowercase_tokens=lowercase_tokens,
                             max_pieces_per_token=pieces_per_token,
                             tn_prob=tn_prob,
                             tp_prob=tp_prob,
                             special_tokens_fix=special_tokens_fix)
train_data = reader.read(train_set)

vocab = Vocabulary.from_instances(train_data,
                                          max_vocab_size={'tokens': 30000,
                                                          'labels': target_vocab_size,
                                                          'd_tags': 2},
                                          tokens_to_add=tokens_to_add)

model_dir = ''

vocab.save_to_files(os.path.join('./models-debug', 'vocabulary'))
print("Data is loaded")




