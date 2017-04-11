clean:
	rm -f db.sqlite3

db_setup:
	./manage.py migrate --noinput
	./manage.py createsuperuser

make_fixtures:
	./manage.py create_users
	./manage.py create_posts
	./manage.py create_photos

all: clean create_database make_fixtures
