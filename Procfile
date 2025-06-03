web: python manage.py collectstatic --noinput && gunicorn cyber_security_club_site.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --threads 8 --timeout 0
