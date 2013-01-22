update_i18n:
	pybabel extract -F babel.cfg -o messages.pot .
	pybabel update -i messages.pot -d i18n -l en
	pybabel compile -d i18n
