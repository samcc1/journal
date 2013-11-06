import datetime
from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from MyJournal.forms import NewJournalEntryForm
from MyJournal.models import JournalEntry

@login_required
def home(request):
    return render(request, 'home.html')

    
@login_required
def home(request):
    if request.method == 'POST':
        form = NewJournalEntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.user = request.user
            new_entry.save()
            response = render(request, "journal_entry.html", {'journal_entry': new_entry})
            response['X-addJournalEntryStatus'] = 'success'
        else:
            response = render(request, "journal_entry_input.html", {'form': form})
            response['X-addJournalEntryStatus'] = 'failed'
        return response
    else:
        form = NewJournalEntryForm(initial={'date': datetime.date.today()})
    
    entries = JournalEntry.objects.filter(user=request.user)
    return render(request, "home.html", {'journal_entries': entries, 'form': form})
