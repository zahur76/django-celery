from django_celery.celery import app

@app.task(bind=True)
def debug_task(self):
    print('Celery is working')