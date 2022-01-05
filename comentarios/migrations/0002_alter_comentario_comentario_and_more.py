# Generated by Django 4.0 on 2021-12-21 16:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='data_comentario',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='email_comentario',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nome_comentario',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='post_comentario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post', verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='publicado_comentario',
            field=models.BooleanField(default=False, verbose_name='Publicado'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='usuario_comentario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user', verbose_name='Usuario'),
        ),
    ]