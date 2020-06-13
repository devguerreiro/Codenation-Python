from django.db import models


class GroupUser(models.Model):
    group = models.ForeignKey(
        "Group", related_name="groupuser", on_delete=models.CASCADE
    )
    user = models.ForeignKey("User", related_name="groupuser", on_delete=models.CASCADE)
