from celery.task import task, Task

from twontw.services.send_data import SendUrlToQueue


@task(name='MoveToQueueTask', base=Task, queue='move-to-queue', ignore_result=True, bind=True)
def move_to_queue_task(*args, **kwargs):
    instance = SendUrlToQueue()
    instance.procces_data()



