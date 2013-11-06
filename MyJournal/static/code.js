
function submit_new_journal_entry() {
    $.post("", $("#add_journal_entry").serialize(), function (data) {
        $("#journal_entries").prepend(data).children(":first").hide().slideDown();
    });
    return false;
}

$(function () {
    $("#add_journal_entry").submit(submit_new_journal_entry);
});
