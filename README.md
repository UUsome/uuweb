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



https://juejin.cn/post/6844904070939951117#heading-7 	


touch /www/uwsgi9090.log

conf/nginx.conf
server {
        listen       80;
        server_name  localhost;
        
        location / {            
            include  uwsgi_params;
            uwsgi_pass  127.0.0.1:9090; #必须和uwsgi中的设置一致
            uwsgi_param UWSGI_SCRIPT demosite.wsgi; #入口文件，即wsgi.py相对于项目根目录的位置，“.”相当于一层目录
            uwsgi_param UWSGI_CHDIR /demosite;#项目根目录
            index  index.html index.htm;
            client_max_body_size 35m;
        }
    }

作者：极客开发者
链接：https://juejin.cn/post/6844904070939951117
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。