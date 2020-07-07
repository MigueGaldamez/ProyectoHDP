
$("#id_departamento").change(function () {
  //alert('llega')
  var url = $("#ReporteForm").attr("data-municipios-url");
  var departamentoId = $(this).val();

  $.ajax({
    url: url,
    data: {
      'departamento': departamentoId
    },
    success: function (data) {
      $("#id_municipio").html(data);
    }
  });
});

function dropdownChange() { 

  if (document.getElementById('eliminados').checked) 
  {
      document.getElementById('id_eliminado').value = "";
      //alert('SI')
  } else {
      document.getElementById('id_eliminado').value = 0;
  }
} 