# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 15:19
from __future__ import unicode_literals

import app.catalog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('name', models.CharField(help_text='Facility name (e.g. "SNS" or "HFIR")', max_length=32, primary_key=True, serialize=False, verbose_name='facility name')),
                ('description', models.CharField(help_text='Facility description (e.g. "Spallation Neutron Source")', max_length=1024, verbose_name='facility description')),
                ('active', models.BooleanField(default=False, help_text='Whether the facility is active and working in the dashboard', verbose_name='facility is active')),
            ],
            bases=(app.catalog.models.AutoRepr, models.Model),
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('name', models.CharField(help_text='Instrument name (e.g. "EQSANS" or "BioSANS")', max_length=32, primary_key=True, serialize=False, verbose_name='instrument name')),
                ('description', models.CharField(help_text='Instrument description (e.g. "Backscattering Spectrometer")', max_length=1024, verbose_name='instrument description')),
                ('beamline', models.CharField(help_text='Beamline that goes into instrument (e.g. "BL-2")', max_length=32, verbose_name='instrument beamline')),
                ('type', models.CharField(help_text='Instrument type (e.g. "SANS")', max_length=32, verbose_name='instrument type')),
                ('icat_name', models.CharField(help_text='Name used for querying ICAT server (e.g. "EQSANS")', max_length=32, verbose_name='instrument icat name')),
                ('ldap_name', models.CharField(help_text='Name used for querying LDAP server', max_length=32, verbose_name='instrument ldap name')),
                ('drive_name', models.CharField(help_text='Name used for loading files from shared filesystem', max_length=32, verbose_name='instrument drive name')),
                ('reduction_available', models.BooleanField(default=False, help_text='Whether the instrument can do reductions', verbose_name='instrument can do reductions')),
                ('active', models.BooleanField(default=False, help_text='Whether the instrument is active and working in the dashboard', verbose_name='instrument is active')),
                ('facility', models.ForeignKey(help_text='The facility the instrument is at (e.g. "SNS")', on_delete=django.db.models.deletion.CASCADE, related_name='instruments', to='catalog.Facility', verbose_name="instrument's facility")),
            ],
            bases=(app.catalog.models.AutoRepr, models.Model),
        ),
    ]
