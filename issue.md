### Model trained on other language generates vocabulary containing only English words

I trained the model on the Oscar **Tamil** dataset. I changed the `weights_name` in `train.py` and `predict.py` as discussed in #94. I tried the default RoBERTA model. I also tried XLM (xlm-roberta-base), which was pre-trained on a multilingual dataset that includes Tamil. I used errant for preprocessing the dataset. I trained the model for three epochs with 10000 updates_per_epoch

The generated vocabulary contains only English words and special characters and no Tamil words or characters. Also, the model doesn't predict any correction on the dataset.

Preprocessed data looks like this.

```
S பொழுது சாய்ந்து வெகு நேரமாகிவிட்டது
A 0 1|||R:OTHER|||பொலுது|||REQUIRED|||-NONE-|||0

S கூலி வேலைக்குப் போயிருந்த 'சித்தாள் ' பெண்கள் எல்லோரும் வீடு திரும்பி விட்டார்கள்
A 5 6|||R:OTHER|||பென்கள்|||REQUIRED|||-NONE-|||0
A 6 7|||R:OTHER|||எழ்ழோரும்|||REQUIRED|||-NONE-|||0
A 9 10|||R:PUNCT|||விட்டார்கல்|||REQUIRED|||-NONE-|||0
```

labels.txt in [vocabulary ](https://drive.google.com/drive/folders/1Yxc1iupZegU9Fa6MnwNuuGtuS4XezYeq?usp=sharing) looks like this

```
$REPLACE_.
$APPEND_/
$TRANSFORM_VERB_VBZ_VBN
$APPEND_8
$REPLACE_of
$REPLACE_you
$REPLACE_(
$APPEND_)
$REPLACE_have
$APPEND_of
$APPEND_&
$REPLACE_read
$APPEND_by
$APPEND_using
$APPEND_new
```
