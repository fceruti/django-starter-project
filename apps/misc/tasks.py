from celery import task


@task
def task_dummy(a, b):
    print("Called task_dummy with a:%s b:%s" % (a, b))
