function register_new_journal_entry_handler() {
    $("#add_journal_entry").submit(submit_new_journal_entry);
}


function submit_new_journal_entry() {
    $.post("", $("#add_journal_entry").serialize(), function (data, textStatus, jqXHR) {
        if (jqXHR.getResponseHeader('X-addJournalEntryStatus') == 'success') {
            $("#journal_entries").prepend(data).children(":first").hide().slideDown();
        } else {
            $("#form_container").html(data);
            register_new_journal_entry_handler();
        }
    });
    return false;
}

$(function () {
    register_new_journal_entry_handler();
});
