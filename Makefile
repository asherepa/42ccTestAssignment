VENV_PATH=/home/dustin/.virtualenvs/_42test_dustin

test:
	# activate our virtualenv environment
	. $(VENV_PATH)/bin/activate
	./manage.py test --pythonpath="`pwd`" accounts
clean:
	find -type f -name "*.pyc" -delete
