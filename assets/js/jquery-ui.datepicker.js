$(document).ready(function() {
    $("#datepicker").datepicker({
        changeYear: true,
        dateFormat: "yy-mm-dd",
        yearRange: "c-100:c+0",
        maxDate: "+2D"
    });
});