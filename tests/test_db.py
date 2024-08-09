from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(username='joão', password='senha', email='teste@example.com')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'joão'))

    assert user.username == 'joão'
