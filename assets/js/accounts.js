$(document).ready(function () {
    var options = {
        dataType: "json",
        success: showResponse,
        timeout: 3000
    };

    $('#userform').submit(function(e) {
        var message_area = $("#sendwrapper");
        message_area.empty();
        message_area.prepend('<span>Sending message ...</span>')
            .css('color', 'black')
            .show();
        $(this).ajaxSubmit(options);
        $("#userform input, select, textarea").attr('disabled', 'disabled');
        e.preventDefault();
    });

    function showResponse(responseText, statusText)  {
        $('#userform input, select, textarea').removeAttr('disabled');
        var message_area = $("#sendwrapper");
        message_area.empty();
        if (responseText['success']) {
            message_area
                .prepend('<span>Changes have been saved</span>')
                .fadeOut(3000);
        } else {
            $.each(responseText['errors'], function(key, val) {
                console.log("key:" + key + " val:" + val);
            });
            message_area
                .prepend('<span>An error occurred while sending the form!</span>')
                .css('color', 'red');
        }
    };
});