# Generated by Django 2.2.2 on 2020-04-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20200404_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='relation',
            field=models.ManyToManyField(blank=True, null=True, related_name='_journal_relation_+', to='journal.Journal', verbose_name='関連記事(複数選択可)'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='tags',
            field=models.ManyToManyField(blank=True, to='journal.Tag', verbose_name='タグ(複数選択可)'),
        ),
    ]
