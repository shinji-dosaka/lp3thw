cd ~
python

pip list

mkdir .venvs
python -m venv --system-site-packages .venvs\lpthw

Set-ExecutionPolicy remotesigned -scope currentUser

.\.venvs\lpthw\Scripts\activate
pip install pytest

mkdir projects
cd projects/
mkdir skeleton
cd skeleton
mkdir bin NAME tests docs

new-item -type file NAME\__init__.py
new-item -type file tests\__init__.py

cd ..  # NAME/の一つ上に移動する
ls     # OK! 正しい場所にいる
pytest

deactivate
