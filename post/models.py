<<<<<<< HEAD
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

=======
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    passwd = models.CharField(max_length=20, blank=True, null=True)
    nickname = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26

class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'category'
<<<<<<< HEAD


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


class Post(models.Model):
    pn = models.IntegerField(db_column='PN', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    head_image = models.TextField(blank=True, null=True)
    author = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='author', to_field='nickname', blank=True,
                               null=True)
=======
        
        # 리뷰 작성 페이지 + 카테고리
        # 로그인 회원가입
        # 장고 검색 기능
        
class Post(models.Model):
    pn = models.AutoField(db_column='PN', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True, auto_now_add = True)
    content = models.TextField(max_length=1000, blank=True, null=True)
    head_image = models.ImageField(upload_to="post/images/",blank=True, null=True)
    author = models.ForeignKey('User', models.DO_NOTHING, db_column='author', to_field='nickname', blank=True, null=True)
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'
<<<<<<< HEAD


class UserInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    passwd = models.CharField(max_length=20, blank=True, null=True)
    nickname = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'
=======
        
    def __str__ (self):
        return self.title
    
    def get_absolute_url(self):
        return f'{self.pk}/'

    def get_image_url(self):
        return self.head_image[:].decode()
        
class Photo(models.Model):
    postnum = models.ForeignKey('Post', models.DO_NOTHING, db_column='postnum', blank=True, null=True)
    image = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photo'
        
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
