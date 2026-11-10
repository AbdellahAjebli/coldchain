from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DHT', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dht11',
            old_name='temp',
            new_name='temperature',
        ),
        migrations.RenameField(
            model_name='dht11',
            old_name='hum',
            new_name='humidity',
        ),
        migrations.RenameField(
            model_name='dht11',
            old_name='dt',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='dht11',
            name='temperature',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dht11',
            name='humidity',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dht11',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

