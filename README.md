环境：
Python 3.11.3
Django         4.2.3
PyMySQL        1.1.0
Markdown       3.4.3






## 问题
1，日程需要登录。否则从其它地方跳转报错。
2，blog 看博文 detail相当慢

python manage.py shell

python manage.py startapp blog
python manage.py startapp plan

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser