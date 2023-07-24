# Generated by Django 4.2.3 on 2023-07-23 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='文章类型')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '文章类型',
                'verbose_name_plural': '文章类型',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('source_id', models.CharField(max_length=25, verbose_name='文章id或source名称')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='评论时间')),
                ('user_name', models.CharField(max_length=25, verbose_name='评论用户')),
                ('url', models.CharField(max_length=100, verbose_name='链接')),
                ('comment', models.CharField(max_length=500, verbose_name='评论内容')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30, verbose_name='标签名称')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_time', models.DateField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('digest', models.TextField(blank=True, null=True)),
                ('author', models.CharField(max_length=64, verbose_name='作者')),
                ('view', models.BigIntegerField(default=0)),
                ('comment', models.BigIntegerField(default=0)),
                ('picture', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='文章类型')),
                ('tag', models.ManyToManyField(to='blog.tag')),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
    ]