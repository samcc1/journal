from django import forms
from MyJournal.models import JournalEntry

class NewJournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['date', 'title', 'content']

