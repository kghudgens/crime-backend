from django.db import models
from django.contrib.auth.models import User
import us

state_choices = []

for v in us.states.STATES:
    state_tuple = ()
    state = us.states.lookup(str(v))
    state_tuple += (state.abbr, str(v))
    state_choices.append(state_tuple)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=2, choices=state_choices)

    def __str__(self):
        return self.user.first_name
