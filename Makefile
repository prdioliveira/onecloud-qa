clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

setup:
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py loaddata onecloud/fixtures/users.json

dev:
	python manage.py jenkins --pep8-exclude="*migrations*" --pep8-max-line-length=160 --pep8-ignore=E128, E303, E503, E731
