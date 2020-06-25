const $region = $('#cboregion');
const $comuna = $('#cbocomuna');
    
$region.change(function() {
    $comuna.val('');
    
    $comuna.prop('disabled', !Boolean($region.val()));
    $comuna.find('option[data-departamento]').hide();
    $comuna.find('option[data-departamento="' + $region.val() + '"]').show();
});