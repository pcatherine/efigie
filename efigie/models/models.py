# import re

# from django.db import models
# from django.core import validators
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
# from django.conf import settings

# # Create your models here.
# class User(AbstractBaseUser, PermissionsMixin):

#   username = models.CharField(
#         'Usuário', max_length=30, unique=True, 
#         validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
#             'O nome de usuário não pode conter espaços. Pode conter letras, digitos ou os '
#             'seguintes caracteres: @ . + - _', 'invalid')]
#     )

#   email = models.EmailField('E-mail', unique=True)
#   name = models.CharField('Nome', max_length=100)
#   phone_area_code = models.CharField(verbose_name='DDD', max_length=3, blank=True, default='000')
#   phone_numer = models.CharField(verbose_name='Telefone', max_length=9,  blank=True )
#   profession = models.CharField(verbose_name='Profissão', max_length=70, blank=True)
#   mini_about = models.CharField(verbose_name='Mini descrição', max_length=200, blank=True)
#   about = models.TextField(verbose_name='Sobre', blank=True)
  
#   #Address Fields
#   #--------------
#   zip_code = models.CharField(verbose_name='CEP', blank=True, max_length=9)
#   address = models.CharField(verbose_name='Endereço', max_length=150,blank=True)
#   address_number = models.IntegerField(verbose_name='Número', blank=True, default=0)
#   address_complement = models.CharField(verbose_name='Complemento', max_length=100,blank=True)
#   address_district = models.CharField(verbose_name='Bairro', max_length=100,blank=True)
#   address_city = models.CharField(verbose_name='Cidade', max_length=150, blank=True)
#   #--------------

#   #Social Media
#   facebook = models.CharField(verbose_name = 'Facebook', max_length=150, blank=True)
#   twitter = models.CharField(verbose_name = 'Twitter', max_length=150, blank=True)
#   linkedin = models.CharField(verbose_name = 'Linkedin', max_length=150, blank=True)
#   #--------------
  
#   is_active = models.BooleanField('Está ativo?', blank=True, default=True)
#   is_developer = models.BooleanField('É Desenvolvedor?', blank=True, default=False)
#   is_suport = models.BooleanField('É Suporte?', blank=True, default=False)
#   is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
#   date_joined = models.DateTimeField('Data de Cadastro', auto_now_add=True)
#   date_updated = models.DateTimeField('Data de Atualização', auto_now=True, blank=True)
#   #last_accessed = models.DateTimeField('Último Acesso', auto_now_add=True)
#   user_image = models.ImageField(upload_to='images', verbose_name='Imagem', null=True, blank=True)
#   objects = UserManager()

#   USERNAME_FIELD = 'username'
#   REQUIRED_FIELDS = ['email']

#   def __str__(self):
#     if self.name:
#       return self.name
#     else:
#       return self.username

#   def get_short_name(self):
#     return self.username

#   def get_full_name(self):
#     return str(self.name)

#   class Meta:
#     verbose_name = 'Usuário'
#     verbose_name_plural = 'Usuários'


# class UserPasswordReset(models.Model):

#   user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='resets')
#   key = models.CharField('Chave', max_length=100, unique=True)
#   created_at = models.DateTimeField('Criado em', auto_now_add=True)
#   confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

#   def __str__(self):
#     return '{0} em {1}'.format(self.user, self.created_at)

#   class Meta:
#     verbose_name = 'Nova Senha'
#     verbose_name_plural = 'Novas Senhas'
#     ordering = ['-created_at']
