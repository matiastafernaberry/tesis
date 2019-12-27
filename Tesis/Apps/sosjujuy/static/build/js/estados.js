$( document ).ready(function() {
	
	var formNotificacion = document.getElementById('notificacionForm');
	if (formNotificacion != null){
		//id_escala
		localStorage.removeItem("goTo");

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

		$(document).on('click', "#icon_prestador", function(e) {
			e.preventDefault();
			var goTo = {"goTo": "/notificacion/"};
			localStorage.setItem('goTo', JSON.stringify(goTo));
			window.location.replace("/prestador/");
		});

		$(document).on('click', "#icon_beneficiario", function(e) {
			e.preventDefault();
			var goTo = {"goTo": "/notificacion/"};
			localStorage.setItem('goTo', JSON.stringify(goTo));
			window.location.replace("/beneficiario/");
		});			
	};

});