$(document).ready(function () {
    var options = {
        dataType: "json",
        success: showResponse,
        timeout: 3000
    };

    $('#userform').submit(function(e) {
        $("#sendwrapper").prepend('<span>Sending message ...</span>');
        $(this).ajaxSubmit(options);
        $("#userform input, select, textarea").attr('disabled', 'disabled');
        e.preventDefault();
    });

    function showResponse(responseText, statusText)  {
        console.log(responseText + " " + statusText)
        $('#userform input, select, textarea').removeAttr('disabled');
        if (responseText['success']) {
            $("#sendwrapper span").remove();
            $("#sendwrapper")
                .prepend('<span>Changes have been saved</span>')
                .fadeOut(5000);
        } else {
            $.each(responseText['errors'], function(key, val) {
                console.log("key:" + key + " val:" + val);
            });
            $("#sendwrapper")
                .prepend('<span>Changes have been saved</span>')
                .css("color: red;")
                .fadeOut(5000);
        }
    };
});