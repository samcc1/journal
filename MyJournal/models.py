from django.db import models
from django.contrib.auth.models import User

class JournalEntry(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    title = models.CharField(max_length=512)
    content = models.TextField()

    def __unicode__(self):
        return '(user = %s, date = %s, title = %s, content = %s' % (repr(self.user), repr(self.date), self.title, self.content)
