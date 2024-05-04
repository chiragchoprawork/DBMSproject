# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.customer_name

class AcdChecking(models.Model):
    a_uid = models.OneToOneField('AcdSafeAcnt', models.DO_NOTHING, db_column='a_uid', primary_key=True, db_comment='SAFE Unique Account ID')  # The composite primary key (a_uid, acct_type) found, that is not supported. The first column is selected.
    acct_type = models.ForeignKey('AcdSafeAcnt', models.DO_NOTHING, db_column='acct_type', to_field='acct_type', related_name='acdchecking_acct_type_set', db_comment='Account Type - Checking (C)/ Savings (S)/ Loan (L)')
    acct_no = models.BigIntegerField(unique=True, db_comment='Checking Account Unique Account Number')
    date_open = models.DateTimeField(db_comment='Account Opening Date')
    serv_charge = models.DecimalField(max_digits=6, decimal_places=2, db_comment='Account Service Charge')

    class Meta:
        managed = False
        db_table = 'acd_checking'
        unique_together = (('a_uid', 'acct_type'),)


class AcdCustomer(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_fname = models.CharField(max_length=30)
    c_lname = models.CharField(max_length=30)
    c_street = models.CharField(max_length=30)
    c_city = models.CharField(max_length=30)
    c_state = models.CharField(max_length=2)
    c_zipcode = models.CharField(max_length=5)
    a_uid = models.ForeignKey('AcdSafeAcnt',on_delete =models.DO_NOTHING,db_column='a_uid', to_field='a_uid')
    # acct_type = models.ForeignKey('AcdSafeAcnt', on_delete =models.CASCADE, db_column='acct_type', to_field='acct_type', related_name='acdcustomer_acct_type_set')

    class Meta:
        managed = False
        db_table = 'acd_customer'
        # unique_together = (('a_uid', 'acct_type'),)
        
class AcdSafeAcnt(models.Model):
    a_uid = models.BigIntegerField(primary_key=True, db_comment='SAFE Unique Account ID')
    acct_type = models.CharField(max_length=2, db_comment='Account Type - Checking (C)/ Savings (S)/ Loan (L)',unique=True)
    acct_name = models.CharField(max_length=30, db_comment='Account Name')
    a_street = models.CharField(max_length=30, db_comment='Account Street Address')
    a_city = models.CharField(max_length=30, db_comment='Account City Location')
    a_state = models.CharField(max_length=2, db_comment='Account State Code - Ex: New York: NY')
    a_zipcode = models.CharField(max_length=5, db_comment='Account Zipcode')

    class Meta:
        managed = False
        db_table = 'acd_safe_acnt'
        unique_together = (('a_uid', 'acct_type'),)



class AcdHome(models.Model):
    a_uid = models.OneToOneField('AcdLoan', models.DO_NOTHING, db_column='a_uid', primary_key=True, db_comment='SAFE Unique Account ID')  # The composite primary key (a_uid, acct_type) found, that is not supported. The first column is selected.
    acct_type = models.ForeignKey('AcdLoan', models.DO_NOTHING, db_column='acct_type', to_field='acct_type', related_name='acdhome_acct_type_set', db_comment='Account Type - Checking (C)/ Savings (S)/ Loan (L)',unique=True)
    hl_uid = models.IntegerField(unique=True, db_comment='Home Loan Unique Loan ID')
    date_open = models.DateTimeField(db_comment='Home Loan Account Opening Date')
    built_year = models.SmallIntegerField(db_comment='Home Built Year')

    class Meta:
        managed = False
        db_table = 'acd_home'
        unique_together = (('a_uid', 'acct_type'),)


class AcdInstitute(models.Model):
    inst_code = models.IntegerField(primary_key=True, db_comment='Unique Institute Code')
    inst_name = models.CharField(max_length=30, db_comment='Institute Name (University Name)')

    class Meta:
        managed = False
        db_table = 'acd_institute'


class AcdInsurance(models.Model):
    ins_acct_no = models.BigIntegerField(primary_key=True, db_comment='Home Insurance Unique Account Number')
    ins_company = models.CharField(max_length=30, db_comment='Insurance Company Name')
    ins_street = models.CharField(max_length=30, db_comment='Insurance Street Address')
    ins_city = models.CharField(max_length=30, db_comment='Insurance City Location')
    ins_state = models.CharField(max_length=2, db_comment='Insurance State Code- Ex: New York: NY')
    ins_zipcode = models.CharField(max_length=5, db_comment="Insurance Company's Zipcode")
    yearly_prm = models.DecimalField(max_digits=8, decimal_places=2, db_comment='Insurance Yearly Premium')
    hl_uid = models.OneToOneField(AcdHome, models.DO_NOTHING, db_column='hl_uid')

    class Meta:
        managed = False
        db_table = 'acd_insurance'


class AcdLoan(models.Model):
    a_uid = models.OneToOneField('AcdSafeAcnt', models.DO_NOTHING, db_column='a_uid', primary_key=True, db_comment='SAFE Unique Account ID')  # The composite primary key (a_uid, acct_type) found, that is not supported. The first column is selected.
    acct_type = models.ForeignKey('AcdSafeAcnt', models.DO_NOTHING, db_column='acct_type', to_field='acct_type', related_name='acdloan_acct_type_set', db_comment='Account Type - Checking (C)/ Savings (S)/ Loan (L)',unique=True)
    acct_no = models.BigIntegerField(db_comment='Loan Account Unique Account Number')
    loan_type = models.CharField(max_length=2, db_comment='Loan Type - Student (SL)/ Home (HL)/ Personal (PL)')
    loan_amt = models.DecimalField(max_digits=10, decimal_places=2, db_comment='OVERALL LOAN AMOUNT ')
    loan_rate = models.DecimalField(max_digits=4, decimal_places=2, db_comment='LOAN INTEREST RATE')
    loan_months = models.SmallIntegerField(db_comment='LOAN DURATION')
    loan_payment = models.DecimalField(max_digits=8, decimal_places=2, db_comment='LOAN REPAYMENT PER MONTH')

    class Meta:
        managed = False
        db_table = 'acd_loan'
        unique_together = (('a_uid', 'acct_type'), ('acct_no', 'loan_type'),)


class AcdPersonal(models.Model):
    a_uid = models.OneToOneField(AcdLoan, models.DO_NOTHING, db_column='a_uid', primary_key=True, db_comment='SAFE Unique Account ID')  # The composite primary key (a_uid, acct_type) found, that is not supported. The first column is selected.
    acct_type = models.ForeignKey(AcdLoan, models.DO_NOTHING, db_column='acct_type', to_field='acct_type', related_name='acdpersonal_acct_type_set', db_comment='Account Type - Checking (C)/ Savings (S)/ Loan (L)',unique=True)
    pl_uid = models.IntegerField(unique=True, db_comment='Personal Loan Unique ID')
    date_open = models.DateTimeField(db_comment='Personal Loan Account Opening Date')

    class Meta:
        managed = False
        db_table = 'acd_personal'
        unique_together = (('a_uid', 'acct_type'),)





class AcdSavings(models.Model):
    a_uid = models.OneToOneField(AcdSafeAcnt, models.DO_NOTHING, db_column='a_uid', primary_key=True, db_comment='SAFE Unique Account ID')  # The composite primary key (a_uid, acct_type) found, that is not supported. The first column is selected.
    acct_type = models.ForeignKey(AcdSafeAcnt, models.DO_NOTHING, db_column='acct_type', to_field='acct_type', related_name='acdsavings_acct_type_set', db_comment='Account Type - Checking (C)/ Savings (S)/ Loan (L)',unique=True)
    acct_no = models.BigIntegerField(unique=True, db_comment='Savings Account Unique Account Number')
    date_open = models.DateTimeField(db_comment='Savings Account Opening Date')
    intrst_rate = models.DecimalField(max_digits=4, decimal_places=2, db_comment='Interest Rate')

    class Meta:
        managed = False
        db_table = 'acd_savings'
        unique_together = (('a_uid', 'acct_type'),)


class AcdStudent(models.Model):
    a_uid = models.OneToOneField(AcdLoan, models.DO_NOTHING, db_column='a_uid', primary_key=True, db_comment='SAFE Unique Account ID')  # The composite primary key (a_uid, acct_type) found, that is not supported. The first column is selected.
    acct_type = models.ForeignKey(AcdLoan, models.DO_NOTHING, db_column='acct_type', to_field='acct_type', related_name='acdstudent_acct_type_set', db_comment='Account Type - Checking (C)/ Savings (S)/ Loan (L)',unique=True)
    sl_uid = models.FloatField(unique=True, db_comment='Student Loan Unique Loan ID')
    date_open = models.DateTimeField(db_comment='Student Loan Account Opening Date')
    student_id = models.CharField(max_length=6, db_comment='Student ID From Institute')
    degree_type = models.CharField(max_length=13, db_comment='Degree Type - Graduate / Undergraduate')
    grad_month = models.CharField(max_length=10, db_comment='Graduation Month')
    grad_year = models.SmallIntegerField(db_comment='Graduation Year')
    inst_code = models.ForeignKey(AcdInstitute, models.DO_NOTHING, db_column='inst_code')

    class Meta:
        managed = False
        db_table = 'acd_student'
        unique_together = (('a_uid', 'acct_type'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CustomersCustomer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customers_customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
