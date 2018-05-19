# Generated by Django 2.0.3 on 2018-05-16 02:39

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('event_code', models.CharField(max_length=50)),
                ('internal_cal_id', models.CharField(blank=True, max_length=50)),
                ('event_name', models.CharField(blank=True, max_length=50)),
                ('project_code', models.CharField(blank=True, max_length=50)),
                ('customer', models.CharField(blank=True, max_length=50)),
                ('event_status', models.CharField(blank=True, max_length=50)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('duration', models.PositiveIntegerField(blank=True, null=True)),
                ('prod_start', models.DateTimeField(blank=True, null=True)),
                ('prod_hours', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('producers_req', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('invite_coming', models.NullBooleanField()),
                ('on_site', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('site_address', models.CharField(blank=True, max_length=255)),
                ('lead_contact', models.CharField(blank=True, max_length=50)),
                ('contact_phone', models.CharField(blank=True, max_length=50)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('link_needed', models.NullBooleanField()),
                ('exp_participants', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('exp_presenters', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('presenters_list', models.TextField(blank=True)),
                ('report_reqs', models.CharField(blank=True, max_length=50)),
                ('record_reqs', models.NullBooleanField()),
                ('original_request', models.URLField(blank=True)),
                ('meeting_link', models.URLField(blank=True)),
                ('meeting_user', models.EmailField(blank=True, max_length=254)),
                ('meeting_password', models.CharField(blank=True, max_length=50)),
                ('audio_type', models.CharField(blank=True, max_length=50)),
                ('tc_number', models.URLField(blank=True)),
                ('tc_participant_pin', models.CharField(blank=True, max_length=50)),
                ('tc_host_pin', models.CharField(blank=True, max_length=50)),
                ('scheduled_by', models.CharField(blank=True, max_length=50)),
                ('production_ready', models.NullBooleanField()),
                ('prod_one_id', models.CharField(blank=True, max_length=50)),
                ('prod_one_email', models.EmailField(blank=True, max_length=254)),
                ('prod_one_confirm', models.NullBooleanField()),
                ('prod_two_id', models.CharField(blank=True, max_length=50)),
                ('prod_two_email', models.EmailField(blank=True, max_length=254)),
                ('prod_two_confirm', models.NullBooleanField()),
                ('event_code_numeric', models.CharField(blank=True, max_length=50)),
                ('cal_name', models.CharField(blank=True, max_length=50)),
                ('docs_link', models.URLField(blank=True)),
                ('prod_one_cell', models.CharField(blank=True, max_length=50)),
                ('prod_two_cell', models.CharField(blank=True, max_length=50)),
                ('client_event_code', models.CharField(blank=True, max_length=50)),
                ('assigned_by', models.CharField(blank=True, max_length=50)),
                ('client_invite_link', models.URLField(blank=True)),
                ('internal_notes', models.TextField(blank=True)),
                ('client_notes', models.TextField(blank=True)),
                ('internal_event_link', models.URLField(blank=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('project_id', models.CharField(blank=True, max_length=100)),
                ('portal_link', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['-modified', '-created'],
            },
        ),
    ]