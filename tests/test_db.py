from fast_zero.models import User


def test_create_user():
    engine = create_engine(
        'sqlite:///database.db'
    )
    user = User(
        username='dunossauro',
        password='senha123',
        email='duno@ssauro.com',
    )
    assert user.username == 'dunossauro'
