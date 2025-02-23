# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 17:53
from __future__ import unicode_literals

import datetime
from datetime import timezone

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_provider', '0015_change_client_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconsent',
            name='date_given',
            field=models.DateTimeField(
                default=datetime.datetime(2016, 6, 10, 17, 53, 48, 889808, tzinfo=datetime.timezone.utc), verbose_name='Date Given'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='_redirect_uris',
            field=models.TextField(
                default=b'', help_text='Enter each URI on a new line.', verbose_name='Redirect URIs'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.CharField(max_length=255, unique=True, verbose_name='Client ID'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_secret',
            field=models.CharField(blank=True, default=b'', max_length=255, verbose_name='Client SECRET'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_type',
            field=models.CharField(
                choices=[(b'confidential', b'Confidential'), (b'public', b'Public')],
                default=b'confidential',
                help_text='<b>Confidential</b> clients are capable of maintaining the confidentiality of their '
                          'credentials. <b>Public</b> clients are incapable.',
                max_length=30,
                verbose_name='Client Type'),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_created',
            field=models.DateField(auto_now_add=True, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(default=b'', max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='response_type',
            field=models.CharField(
                choices=[
                    (b'code', b'code (Authorization Code Flow)'), (b'id_token', b'id_token (Implicit Flow)'),
                    (b'id_token token', b'id_token token (Implicit Flow)')],
                max_length=30,
                verbose_name='Response Type'),
        ),
        migrations.AlterField(
            model_name='code',
            name='_scope',
            field=models.TextField(default=b'', verbose_name='Scopes'),
        ),
        migrations.AlterField(
            model_name='code',
            name='client',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='oidc_provider.Client', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.CharField(max_length=255, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='code',
            name='code_challenge',
            field=models.CharField(max_length=255, null=True, verbose_name='Code Challenge'),
        ),
        migrations.AlterField(
            model_name='code',
            name='code_challenge_method',
            field=models.CharField(max_length=255, null=True, verbose_name='Code Challenge Method'),
        ),
        migrations.AlterField(
            model_name='code',
            name='expires_at',
            field=models.DateTimeField(verbose_name='Expiration Date'),
        ),
        migrations.AlterField(
            model_name='code',
            name='is_authentication',
            field=models.BooleanField(default=False, verbose_name='Is Authentication?'),
        ),
        migrations.AlterField(
            model_name='code',
            name='nonce',
            field=models.CharField(blank=True, default=b'', max_length=255, verbose_name='Nonce'),
        ),
        migrations.AlterField(
            model_name='code',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='rsakey',
            name='key',
            field=models.TextField(help_text='Paste your private RSA Key here.', verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='token',
            name='_id_token',
            field=models.TextField(verbose_name='ID Token'),
        ),
        migrations.AlterField(
            model_name='token',
            name='_scope',
            field=models.TextField(default=b'', verbose_name='Scopes'),
        ),
        migrations.AlterField(
            model_name='token',
            name='access_token',
            field=models.CharField(max_length=255, unique=True, verbose_name='Access Token'),
        ),
        migrations.AlterField(
            model_name='token',
            name='client',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='oidc_provider.Client', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='token',
            name='expires_at',
            field=models.DateTimeField(verbose_name='Expiration Date'),
        ),
        migrations.AlterField(
            model_name='token',
            name='refresh_token',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Refresh Token'),
        ),
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='userconsent',
            name='_scope',
            field=models.TextField(default=b'', verbose_name='Scopes'),
        ),
        migrations.AlterField(
            model_name='userconsent',
            name='client',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='oidc_provider.Client', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='userconsent',
            name='expires_at',
            field=models.DateTimeField(verbose_name='Expiration Date'),
        ),
        migrations.AlterField(
            model_name='userconsent',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
