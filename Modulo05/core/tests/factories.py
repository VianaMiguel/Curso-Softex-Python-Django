import factory
from django.contrib.auth.models import User
from core.models import Tarefa


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    # Cria users únicos: user0, user1, user2...
    username = factory.Sequence(lambda n: f'user{n}')
    # Cria e-mails baseados no username
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')


class TarefaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tarefa

    # Cria automaticamente um User para esta tarefa
    user = factory.SubFactory(UserFactory)
    # Gera uma frase aleatória
    titulo = factory.Faker('sentence', nb_words=4)
    concluida = False

# Use factories:
tarefa = TarefaFactory() # Cria user e tarefa magicamente
usuarios = UserFactory.create_batch(10) # Cria 10 usuários de uma vez