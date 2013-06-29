install:
	pip install -r requirements.txt
	git submodule init
	git submodule update

update_i18n:
	pybabel extract -F babel.cfg -o messages.pot .
	pybabel update -i messages.pot -d translations -l en
	pybabel compile -d translations
