from django import template

register = template.Library()

@register.simple_tag
def version():
  return "0.3.1000" 

@register.simple_tag
def userDeleteTag(user, form):
  confirmation = {'title': "Você tem certeza que deseja fazer isso?",
    'description': 
      '''
        <p>Excluiremos <b>imediatamente</b> todas as chaves relacionados somente a voce, juntamente com todos os seus contatos.</p> 
      ''',
    'url': "/user/delete",
    'button': "Deletar"}

  return confirmation