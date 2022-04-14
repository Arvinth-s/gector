# conda init zsh
sudo apt install unzip
conda activate gector
# rm errant_env -r

python3 -m venv errant_env
source errant_env/bin/activate
pip3 install -U pip setuptools wheel
pip3 install errant
python3 -m spacy download en

pip install Levenshtein
pip install datasets
pip install filelock