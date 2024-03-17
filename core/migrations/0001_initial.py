# Generated by Django 4.2.9 on 2024-01-23 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='O_Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(default='Loading', max_length=255, verbose_name='Name')),
                ('feed_url', models.URLField(unique=True, verbose_name='Feed URL')),
                ('modified', models.CharField(default='', max_length=255, verbose_name='Last Modified')),
                ('etag', models.CharField(default='', max_length=255)),
                ('size', models.IntegerField(default=0, verbose_name='Size')),
                ('valid', models.BooleanField(null=True, verbose_name='Valid')),
                ('update_frequency', models.IntegerField(default=30, verbose_name='Update Frequency(minutes)')),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                   to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Feed',
                'verbose_name_plural': 'Feeds',
            },
        ),
        migrations.CreateModel(
            name='T_Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=255, unique=True)),
                ('language', models.CharField(
                    choices=[('English', 'English'), ('Chinese Simplified', 'Chinese Simplified'),
                             ('Chinese Traditional', 'Chinese Traditional'), ('Russian', 'Russian'),
                             ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Czech', 'Czech'), ('Danish', 'Danish'),
                             ('German', 'German'), ('Spanish', 'Spanish'), ('French', 'French'),
                             ('Indonesian', 'Indonesian'), ('Italian', 'Italian'), ('Hungarian', 'Hungarian'),
                             ('Norwegian Bokmal', 'Norwegian Bokmal'), ('Dutch', 'Dutch'), ('Polish', 'Polish'),
                             ('Portuguese', 'Portuguese'), ('Swedish', 'Swedish'), ('Turkish', 'Turkish')],
                    max_length=50, verbose_name='Language')),
                ('status', models.BooleanField(null=True, verbose_name='Translation Status')),
                ('translate_title', models.BooleanField(default=True, verbose_name='Translate Title')),
                ('translate_content', models.BooleanField(default=False, verbose_name='Translate Content')),
                ('total_tokens', models.IntegerField(default=0, verbose_name='Tokens Cost')),
                ('total_characters', models.IntegerField(default=0, verbose_name='Characters Cost')),
                ('modified', models.CharField(default='', max_length=255, verbose_name='Last Modified')),
                ('size', models.IntegerField(default=0, verbose_name='Size')),
                ('o_feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.o_feed')),
            ],
            options={
                'verbose_name': 'Translate Feed',
            },
        ),
        migrations.AddConstraint(
            model_name='t_feed',
            constraint=models.UniqueConstraint(fields=('o_feed', 'language'), name='unique_o_feed_lang'),
        ),
    ]