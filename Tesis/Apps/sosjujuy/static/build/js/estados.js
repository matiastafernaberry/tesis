$( document ).ready(function() {
	var formBeneficiarios = document.getElementById('notificacionForm');
	if (formBeneficiarios != null){
		//id_escala
		$('#id_escalaDos').attr("disabled", false);
		$(document).on('change', $("#id_escala"), function() {
			valSelected = $("#id_escala option:selected").val();
			if (valSelected == "Actividades de Extension"){
				$('#id_escalaDos option[value="Reporte"]');
				$('#id_escalaDos').attr("disabled", true);
			}
			if (valSelected == "Beneficiarios"){
				$('#id_escalaDos option[value="Reporte"]');
				$('#id_escalaDos').attr("disabled", true);
			}
			if (valSelected == "Atencion y Derivacion"){
				$('#id_escalaDos option[value="Reporte"]');
				$('#id_escalaDos').attr("disabled", true);
			}
			//console.log(valSelected);
		});
	};

});