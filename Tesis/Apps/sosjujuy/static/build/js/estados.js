function escalaSelected(){
	$('#id_escalaDos').attr("disabled", false);
	valSelected = $("#id_escala option:selected").val();
	//console.log("as");
	if (valSelected == "Actividades de Extension"){
		$('#id_escalaDos')
		    .find('option')
		    .remove()
		    .end()
		    .append('<option value="" selected=selected>----------</option>')
		    .val('')
		    .append('<option value="Reporte">Reporte</option>')
		    .val('Reporte')
		    .append('<option value="Solicitud">Solicitud</option>')
		    .val('Solicitud')
		;
		$('#id_escalaDos option[value=""]').prop('selected', true);
	}
	if (valSelected == "Beneficiarios"){
		$('#id_escalaDos')
		    .find('option')
		    .remove()
		    .end()
		    .append('<option value="" selected=selected>----------</option>')
		    .val('')
		    .append('<option value="Pedido Extraordinario">Pedido Extraordinario</option>')
		    .val('Pedido Extraordinario')
		    .append('<option value="Solicitud de Audiencia">Solicitud de Audiencia</option>')
		    .val('Solicitud de Audiencia')
		;
		$('#id_escalaDos option[value=""]').prop('selected', true);
	}
	if (valSelected == "Atencion y Derivacion"){
		$('#id_escalaDos')
		    .find('option')
		    .remove()
		    .end()
		    .append('<option value="" selected=selected>----------</option>')
		    .val('')
		    .append('<option value="Reporte">Reporte</option>')
		    .val('Reporte')
		;
		$('#id_escalaDos option[value=""]').prop('selected', true);
	}
	//console.log(valSelected);
}

$( document ).ready(function() {
	if ($('#id_escala option:selected')){
		escalaSelected();
	}
	var formNotificacion = document.getElementById('notificacionForm');
	if (formNotificacion != null){
		//id_escala
		localStorage.removeItem("goTo");
		
		$(document).on('change', "#id_escala", function() {
			escalaSelected();
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



function alerta() {
    var mensaje;
    var opcion = confirm("¿Esta seguro que quiere guardar?");
    if (opcion == true) {
        mensaje = "Has clickado OK";
	} else {
	    mensaje = "Has clickado Cancelar";
	}
	document.getElementById("ejemplo").innerHTML = mensaje;
}