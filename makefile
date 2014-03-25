install:
	pip install -r requirements.txt

init:
	git submodule init
	git submodule update
	bash -c 'for file in `find . -name "*.sample" -not -path "./.git/*"`; do cp $$file $${file/.sample/}; done'

update_i18n:
	pybabel extract -F babel.cfg -o messages.pot .
	pybabel update -i messages.pot -d translations -l en
	pybabel compile -d translations
