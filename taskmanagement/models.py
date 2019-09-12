from django.db import models


class Task(models.Model):
    STATUS_CHOICES = (
        (0, 'To_list'),  # To_list
        (1, 'Doing'),  # Doing
        (2, 'Done')  # Done
    )

    SYNC_CHOICES = (
        (0, 'sync with'),
        (1, 'required sync')
    )

    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=0)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    mobile_id = models.CharField(max_length=20, blank=False)
    sync = models.SmallIntegerField(choices=SYNC_CHOICES, default=0)
