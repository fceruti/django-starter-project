from celery import task


@task
def task_dummy(arg_a, arg_b):
    print("Called task_dummy with a:%s b:%s" % (arg_a, arg_b))
