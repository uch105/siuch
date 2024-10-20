$('#check').click(function() {
    if ($(this).is(':checked')) {
        $('#proceed').removeAttr('disabled');
    } else {
        $('#proceed').attr('disabled', 'disabled');
    }
});