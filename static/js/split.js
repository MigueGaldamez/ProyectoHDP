$(function() {
    $('<table class="table table-sm table-striped table-hover">').append(
        $('table thead:first-child').clone(), 
        $('table tr').slice(Math.ceil($('table tr').length / 2))
    ).appendTo('#row');
    /*
    $('<table class="table table-sm">').append(
        $('table thead:first-child').clone(), 
        $('table tr').slice(Math.ceil(($('table tr').length / 3)*2))
    ).appendTo('#row2');*/
});
