
test:
	# activate our virtualenv environment
	. $(VIRTUAL_ENV)/bin/activate
	./manage.py test accounts  --pythonpath=`pwd`
clean:
	find -type f -name "*.pyc" -delete
