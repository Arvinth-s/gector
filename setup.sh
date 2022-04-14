# conda init zsh
sudo apt install unzip
conda activate gector
# rm errant_env -r

git clone https://github.com/chrisjbryant/errant.git
cd errant
python3 -m venv errant_env

# add below command manually to terminal
source errant_env/bin/activate
pip3 install -U pip setuptools wheel
pip3 install -e .
python3 -m spacy download en

pip install levenshein
pip install datasets
pip install filelock