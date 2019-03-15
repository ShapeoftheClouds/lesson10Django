# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Owner(models.Model):
    stockid = models.IntegerField(db_column='stockID', primary_key=True)  # Field name made lowercase.
    stockname = models.TextField(db_column='stockName')  # Field name made lowercase.
    ownerlname = models.TextField(db_column='ownerLName')  # Field name made lowercase.
    earnings = models.TextField()
    yearlyearnings = models.TextField(db_column='yearlyEarnings')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'owner'


class Stockspractice(models.Model):
    stockid = models.IntegerField(db_column='stockID', primary_key=True)  # Field name made lowercase.
    stockname = models.TextField(db_column='stockName')  # Field name made lowercase.
    shareno = models.TextField(db_column='shareNo')  # Field name made lowercase.
    earnings = models.TextField()
    yearlyearnings = models.TextField(db_column='yearlyEarnings')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stocksPractice'
