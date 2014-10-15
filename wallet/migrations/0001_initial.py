# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('style', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=1, choices=[(b'T', b'Tiny'), (b'N', b'Normal'), (b'H', b'Huge')])),
                ('color', models.CharField(max_length=1, choices=[(b'B', b'Black'), (b'G', b'Beige'), (b'W', b'White'), (b'R', b'Red')])),
                ('card_slots', models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15)])),
                ('id_slot', models.CharField(max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('coin_pocket', models.CharField(max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('money_slots', models.SmallIntegerField(choices=[(1, 1), (2, 2)])),
                ('embossed_name', models.CharField(help_text=b'Not more than 10 characters', max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
