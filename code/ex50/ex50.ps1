pip install flask

cd projects
mkdir gothonweb
cd gothonweb
mkdir bin
mkdir gothonweb
mkdir tests
mkdir docs
mkdir templates
new-item -type file gothonweb\__init__.py
new-item -type file tests\__init__.py

flask run

$env:FLASK_ENV = "development"
flask run
