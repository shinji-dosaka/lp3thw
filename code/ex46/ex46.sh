pip3 list

mkdir ~/.venvs
python3 -m venv --system-site-packages ~/.venvs/lpthw
. ~/.venvs/lpthw/bin/activate

which python
python

which python3

pip install pytest

mkdir projects
cd projects/
mkdir skeleton
cd skeleton
mkdir bin NAME tests docs

touch NAME/__init__.py
touch tests/__init__.py

cd ..  # NAME/の一つ上に移動する
ls     # OK! 正しい場所にいる
pytest

deactivate
