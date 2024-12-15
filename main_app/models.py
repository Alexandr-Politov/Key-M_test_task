# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.contenttypes.models import ContentType


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)
    code_exp = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = "country"


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = "language"


class NotificationCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = "notification_category"


class NotificationTemplate(models.Model):
    id = models.AutoField(primary_key=True)
    notification_category = models.ForeignKey(
        NotificationCategory, models.SET_NULL, blank=True, null=True
    )
    name = models.CharField(max_length=32, blank=True, null=True)
    txt = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "notification_template"


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("User", models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=510, blank=True, null=True)
    address = models.CharField(max_length=510, blank=True, null=True)
    started = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING)
    archived = models.IntegerField()

    class Meta:
        db_table = "project"


class TranslationString(models.Model):
    id = models.AutoField(primary_key=True)
    content_type = models.ForeignKey(
        ContentType, models.DO_NOTHING, blank=True, null=True
    )
    object_id = models.IntegerField(blank=True, null=True)
    translation_field_id = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "translation_string"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    role_id = models.PositiveIntegerField(blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING)

    class Meta:
        db_table = "user"


class UserNotification(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    notification_template = models.ForeignKey(
        NotificationTemplate, models.DO_NOTHING, blank=True, null=True
    )
    notification_type = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "user_notification"


class UserNotificationOption(models.Model):
    id = models.AutoField(primary_key=True)
    user_notification = models.ForeignKey(
        UserNotification, models.DO_NOTHING, blank=True, null=True
    )
    field_id = models.IntegerField(blank=True, null=True)
    txt = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = "user_notification_option"


class UserNotificationSetting(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    notification_template = models.ForeignKey(
        NotificationTemplate, models.DO_NOTHING, blank=True, null=True
    )
    system_notification = models.IntegerField()
    push_notification = models.IntegerField()

    class Meta:
        db_table = "user_notification_setting"


class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "user_role"
