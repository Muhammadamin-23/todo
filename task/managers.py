from django.db.models import Manager


class TaskTodotManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_done=False, is_delete=False)


class TaskDoneManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_done=True, is_delete=False)


class TaskDeleteManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_done=False, is_delete=True)


class TaskDoneDeletedManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_done=True, is_delete=True)
