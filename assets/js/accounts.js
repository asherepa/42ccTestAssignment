$(document).ready(function() {
    $("#datepicker").datepicker({
        changeMonth: true,
        dateFormat: "yy-mm-dd"
    });

    var options = {
        target: "#ajaxwrapper",
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
        $('#userform input, select, textarea').removeAttr('disabled');
        if (responseText['success']) {
            $("#sendwrapper span").remove();
            $("#sendwrapper")
            .prepend('<span>The form has been successfully saved</span>')
            .toggle(5000);
        } else {
            $.each(responseText['errors'], function(key, val) {
                console.log("key:" + key + " val:" + val);
            });
            alert("There was an error when adding a new data!");
        }
    };
});