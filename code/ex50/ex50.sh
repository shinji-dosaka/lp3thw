pip install flask

cd projects
mkdir gothonweb
cd gothonweb
mkdir bin gothonweb tests docs templates
touch gothonweb/__init__.py
touch tests/__init__.py

flask run

export FLASK_ENV=development
flask run
