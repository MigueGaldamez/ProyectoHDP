
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


$("#id_perfil__departamento").change(function () {
  //alert('llega')
  var url = $("#ReporteForm").attr("data-municipios-url");
  var departamentoId = $(this).val();

  $.ajax({
    url: url,
    data: {
      'departamento': departamentoId
    },
    success: function (data) {
      $("#id_perfil__municipio").html(data);
    }
  });
});

function dropdownChange() { 
 
  if (document.getElementById('eliminados').checked) 
  {
      document.getElementById('id_eliminado').value = "";
      
  } else {
      document.getElementById('id_eliminado').value = 0;
  }
} 


function checkChange() { 

  if (document.getElementById('validar12').checked) 
  {
      document.getElementById('id_is_active').value = 1;
      //alert('SI')
  } else {
      document.getElementById('id_is_active').value = 0;
  }
} 

function checkbox12() { 
  
  if (document.getElementById('aceptado12').checked) 
  {
      document.getElementById('id_estado').value = 1;
      //alert('SI')
  } else {
      document.getElementById('id_estado').value = 2;
  }
}
function acDocFuncion() {
  document.getElementById('id_is_active').value = 0;
}