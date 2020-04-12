function print_result(result){
    $('#output').html(result);
}

$('form').submit(function () {
    $.ajax({
        type: 'POST',
        dataType: 'text',
        url: '/',
        data: $('form').serialize(),
        success: function (result) {
            print_result(result);
        },
        error: function (result) {
            alert(result.responseText);
        },
    });
    return false;
});

window.onload = function(){
    $('form').submit();
}