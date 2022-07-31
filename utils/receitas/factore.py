from random import randint

from faker import Faker


def randi_radio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')


def make_receita():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'descricao': fake.sentence(nb_words=12),
        'tempo_preparo': fake.random_number(digits=2, fix_len=True),
        'unidade_tempo': 'Minutos',
        'porcoes': fake.random_number(digits=2, fix_len=True),
        'unidade_por': 'Porções',
        'comofazer': fake.text(3000),
        'data_cria': fake.date_time(),
        'autor': {
            'nome': fake.first_name(),
            'sobrenome': fake.last_name()
        },
        'categoria': {
            'nome': fake.word()
        },
        'cover': {
            'url': 'http://loremflickr.com/%s/%s/food,cook' % randi_radio()
        },
    }
