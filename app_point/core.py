from django.db import transaction

from app_account.models import User
from app_point.models.point import Point


@transaction.atomic
def add_point(user_id: int, amount: int):
    """ 포인트를 더합니다. """
    user = User.objects.get(pk=user_id)
    point = Point.objects.select_for_update().get(pk=user.point_id)

    point.balance += amount
    point.save()

    return True


@transaction.atomic
def remove_point(user_id: int, amount: int) -> bool:
    """
    포인트를 차감합니다.
    차감하려는 포인트가 현재 가진 포인트보다 크다면 False를 반환
    """
    user = User.objects.get(pk=user_id)
    point = Point.objects.select_for_update().get(pk=user.point_id)

    point.balance -= amount

    if point.balance < 0:
        return False

    point.save()

    return True
