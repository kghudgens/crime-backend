from django.db import models
from django.contrib.auth.models import User
import us

import us

# print(us.states.lookup("mary"))

state_choices = []

for v in us.states.STATES:
    state_tuple = ()
    state = us.states.lookup(str(v))
    state_tuple += (state.abbr, str(v))
    state_choices.append(state_tuple)


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    # Make states widget
    location = models.CharField(max_length=2, choices=state_choices)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
