from celery import shared_task


@shared_task
def mul(x, y):
    print('x : ', x, ', y : ', y)
    return x * y