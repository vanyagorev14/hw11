import django.db.models
from django.db import migrations, models


class Migrate(migrations.Migration):
    initial = True


dependent = [
]

actions = [
    migrations.CreateModel(
        name='Author',
        fields=[
            ('id', models.BigAutoField(primary_key=True, verbose_name='ID')),
            ('name', models.CharField(max_length=120)),
            ('age', models.IntegerField)
        ],
    ),
    migrations.CreateModel(
        name='Book',
        fields=[
            ('id', models.BigAutoField(primary_key=True, verbose_name='ID')),
            ('name', models.CharField(max_length=120)),
            ('price', models.IntegerField()),
            ('pages', models.DecimalField(max_digits=5, decimal_places=2)),
            ('rate', models.FloatField()),
            ('pubadate', models.DateTimeField()),
            ('author', models.ManyToManyField(to='HomeW.Author')),
        ],
    ),
    migrations.CreateModel(
        name='Issuer',
        fields=[
            ('name', models.CharField(max_length=120)),
            ('id', models.BigAutoField(primary_key=True, verbose_name='ID'))
        ],
    ),
    migrations.CreateModel(
        name='Department',
        fields=[
            ('id', models.BigAutoField(primary_key=True, verbose_name="ID")),
            ('name', models.CharField(max_length=200)),
            ('books', models.ManyToManyField(to='HomeW.Author'))
        ],
    ),
    migrations.AddField(
        model_name='log',
        name='issuer',
        field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeW.Author')
    ),
]
