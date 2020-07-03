
$("#id_departamento").change(function () {
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
