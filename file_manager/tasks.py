from time import sleep

from celery import current_task, shared_task

from .models import File


@shared_task()
def file_handling_task(file_id):
    file = File.objects.get(id=file_id)
    try:
        sleep(5)  # do something
    except Exception as e:
        current_task.update_state(
            state='FAILURE',
            meta={'error': e.__str__(), 'exc_type': e.__class__.__name__}
        )
    else:
        file.processed = True
        file.save()
