from .celery import app as celery_app  # import the celery module in the __init__.py file of your project to ensure it is loaded when Django starts.

__all__ = ['celery_app']
