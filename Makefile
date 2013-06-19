MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=_42cc_test_dustin.settings $(MANAGE) test accounts rlogger

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=_42cc_test_dustin.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=_42cc_test_dustin.settings $(MANAGE) syncdb --noinput

syncall:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=_42cc_test_dustin.settings $(MANAGE) syncdb --migrate --noinput

clean:
	find -type f -name "*.pyc" -delete
