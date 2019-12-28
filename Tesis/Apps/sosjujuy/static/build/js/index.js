<<<<<<< HEAD
var tok = $('input[name=csrfmiddlewaretoken]').attr("value");
localStorage.removeItem("pais_provincia");

$( document ).ready(function() {
    var tok = $('input[name=csrfmiddlewaretoken]').attr("value");
	$(document).on('click', "#enviar_form", function() {
		// envio del prestador
		try{
			var textPrestador = $("a[class=chosen-single]")[0].text.replace(/\s/g, '');
		  	var prestadorList = JSON.parse(localStorage.getItem('prestador'));
	        $("<input />").attr("type", "hidden")
	          .attr("name", "prestador")
	          .attr("value", prestadorList[textPrestador])
	          .attr("id", "id_prestador")
	          .attr("data", textPrestador)
	          .appendTo("#notificacionForm");
	    } catch(error) {
  			//console.error(error);
  		}
  		// envio del beneficiario
  		try{
	        var textBeneficiario = $("a[class=chosen-single]")[1].text.replace(/\s/g, '');
		  	var beneficiarioList = JSON.parse(localStorage.getItem('beneficiario2'));	  	
	        $("<input />").attr("type", "hidden")
	          .attr("name", "beneficiario")
	          .attr("value", beneficiarioList[textBeneficiario])
	          .attr("id", "id_beneficiario")
	          .attr("data", textBeneficiario)
	          .appendTo("#notificacionForm");
	    } catch(error) {
  			//console.error(error);
  		}

        $("<input />").attr("type", "hidden")
          .attr("name", "enviar")
          .attr("value", "true")
          .attr("id", "id_enviar")
          .attr("data", "true")
          .appendTo("#notificacionForm");

		$("form").trigger("submit");
	});	

	$(document).on('click', "#guardar_form", function() {
		try{
			var textPrestador = $("a[class=chosen-single]")[0].text.replace(/\s/g, '');
	  		var prestadorList = JSON.parse(localStorage.getItem('prestador'));	  	
	        $("<input />").attr("type", "hidden")
	          .attr("name", "prestador")
	          .attr("value", prestadorList[textPrestador])
	          .attr("id", "id_prestador")
	          .attr("data", textPrestador)
	          .appendTo("#notificacionForm");
	    } catch(error) {
  			//console.error(error);
  		}
  		try{
	        var textBeneficiario = $("a[class=chosen-single]")[1].text.replace(/\s/g, '');
		  	var beneficiarioList = JSON.parse(localStorage.getItem('beneficiario2'));	  	
	        $("<input />").attr("type", "hidden")
	          .attr("name", "beneficiario")
	          .attr("value", beneficiarioList[textBeneficiario])
	          .attr("id", "id_beneficiario")
	          .attr("data", textBeneficiario)
	          .appendTo("#notificacionForm");
	    } catch(error) {
  			//console.error(error);
  		}

		$("form").trigger("submit");
	});	
	// ------(-.-)------- //
=======
$( document ).ready(function() {
    var tok = $('input[name=csrfmiddlewaretoken]').attr("value");
    //console.log(tok);

>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
    $("#beneficiarioForm").submit(function( event ) {
    	var textPais = $("a[class=chosen-single]")[0].text.replace(/\s/g, '');
    	var textProvincia = $("a[class=chosen-single]")[1].text.replace(/\s/g, '');
    	
	  	var paisesList = JSON.parse(localStorage.getItem('paises'));
	  	var provinciaList = JSON.parse(localStorage.getItem('provincias'));
	  	
	  	$("<input />").attr("type", "hidden")
          .attr("name", "pais")
          .attr("value", paisesList[textPais])
<<<<<<< HEAD
          .attr("id", "pais")
=======
          .attr("id", "id_pais")
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
          .attr("data", textPais)
          .appendTo("#beneficiarioForm");

        $("<input />").attr("type", "hidden")
          .attr("name", "provincia")
          .attr("value", provinciaList[textProvincia])
<<<<<<< HEAD
          .attr("id", "provincia")
=======
          .attr("id", "id_provincia")
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
          .attr("data", textProvincia)
          .appendTo("#beneficiarioForm");
	});	

	$("#DerivacionForm").submit(function( event ) {
<<<<<<< HEAD
    	var textBene = $("a[class=chosen-single]")[0].text.replace(/^\s/g, '').replace(/^\s/g, '').replace(/^\s/g, '').replace(/\s$/g, '').replace(/\s$/g, '').replace(/\s$/g, '').replace(/\s$/g, '').split(" ")[0];
	  	var benefiList = JSON.parse(localStorage.getItem('beneficiario'));	  	

	  	var textPres = $("a[class=chosen-single]")[1].text.replace(/^\s/g, '').replace(/^\s/g, '').replace(/^\s/g, '').replace(/\s$/g, '').replace(/\s$/g, '').replace(/\s$/g, '').replace(/\s$/g, '').split(" ")[0];
	  	var presfiList = JSON.parse(localStorage.getItem('prestacion'));	  	

=======
    	var textBene = $("a[class=chosen-single]")[0].text.replace(/\s/g, '');
	  	var benefiList = JSON.parse(localStorage.getItem('beneficiario'));	  	
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
        $("<input />").attr("type", "hidden")
          .attr("name", "beneficiario")
          .attr("value", benefiList[textBene])
          .attr("id", "id_beneficiario")
          .attr("data", textBene)
          .appendTo("#DerivacionForm");
<<<<<<< HEAD

        $("<input />").attr("type", "hidden")
          .attr("name", "prestacion")
          .attr("value", presfiList[textPres])
          .attr("id", "id_prestacion")
          .attr("data", textPres)
          .appendTo("#DerivacionForm");
	});	

=======
	});	

	$("#notificacionForm").submit(function( event ) {
    	var textPrestador = $("a[class=chosen-single]")[0].text.replace(/\s/g, '');
	  	var prestadorList = JSON.parse(localStorage.getItem('prestador'));	  	
        $("<input />").attr("type", "hidden")
          .attr("name", "prestador")
          .attr("value", prestadorList[textPrestador])
          .attr("id", "id_beneficiario")
          .attr("data", textPrestador)
          .appendTo("#notificacionForm");
	});	

	
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
	// si existe el formulario hace el pedido ajax
	var formBeneficiarios = document.getElementById('beneficiarioForm');
	if (formBeneficiarios != null){
	    $.ajax({
		    type:"POST", 
		    url:"/search/", 
		    data:{url:"Z562316", "csrfmiddlewaretoken": tok},
		    success:function(datos){ 
		    	loadBeneficiario(datos);
		    },
		});
<<<<<<< HEAD
		try{
			$.ajax({
			    type:"POST", 
			    url:"/provincias/", 
			    data:{value:"0", "csrfmiddlewaretoken": tok},
			    success:function(datos){ 
			    	loadProvincia(datos);
			    },
			});
		} catch(error) {
  			//console.error(error);
  		}   	
	}
	// si existe el formulario hace el pedido ajax
	var formDerivacion = document.getElementById('DerivacionForm');
	if (formDerivacion != null){
		$.ajax({
		    type:"POST", 
		    url:"/beneficiariosearch/", 
		    data:{url:"Z562316", "csrfmiddlewaretoken": tok},
		    success:function(datos){ 
		    	loadDerivacion(datos);
		    },
		});
		$.ajax({
		    type:"POST", 
		    url:"/prestadorsearch/", 
		    data:{url:"Z562316", "csrfmiddlewaretoken": tok},
		    success:function(datos){ 
		    	loadPrestacion(datos);
=======
		$.ajax({
		    type:"POST", 
		    url:"/provincias/", 
		    data:{url:"Z562316", "csrfmiddlewaretoken": tok},
		    success:function(datos){ 
		    	loadProvincia(datos);
		    },
		});
	}
	// si existe el formulario hace el pedido ajax
	var formDerivacion = document.getElementById('DerivacionForm');
	if (formDerivacion != null){
		$.ajax({
		    type:"POST", 
		    url:"/beneficiariosearch/", 
		    data:{url:"Z562316", "csrfmiddlewaretoken": tok},
		    success:function(datos){ 
		    	loadDerivacion(datos);
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
		    },
		});
	}

	// si existe el formulario hace el pedido ajax
	var notificacionForm = document.getElementById('notificacionForm');
	if (notificacionForm != null){
<<<<<<< HEAD
		//$('#id_estado').prop('disabled', 'disabled');
=======
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
		$.ajax({
		    type:"POST", 
		    url:"/prestadorsearch/", 
		    data:{url:"Z562316", "csrfmiddlewaretoken": tok},
		    success:function(datos){ 
		    	loadPrestador(datos);
		    },
		});
		$.ajax({
		    type:"POST", 
		    url:"/beneficiariosearch/", 
		    data:{url:"Z562316", "csrfmiddlewaretoken": tok},
		    success:function(datos){ 
		    	loadBeneficiarioNotificacion(datos);
		    },
		});
	}
});

<<<<<<< HEAD

function loadBeneficiario(datos){
	var textSelect = $("#id_pais option:selected").text();
	// en el editar esta el select comun
	if (textSelect == "---------"){
=======
function loadBeneficiario(datos){
	var textSelect = $("#id_pais option:selected").text();
	// en el editar esta el select comun
	if (textSelect != "---------"){
		//
	} else {
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
		//console.log(textSelect);
		var valSelect = $("#id_pais option:selected").val();
		//console.log(valSelect);
		$("#id_pais").parent().append(
<<<<<<< HEAD
			`<select data-placeholder="Seleccione un País..." class="chosen-select id_pais" tabindex="2">
=======
			`<select data-placeholder="Elija un País..." class="chosen-select id_pais" tabindex="2">
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
            <option value=""></option>`);

		var paises = {};
		for (x in datos) {
<<<<<<< HEAD
=======
    		//console.log(datos[x]["pk"]);

>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
    		paises[datos[x]["fields"]["nombre"]] = datos[x]["pk"];
    		$(".chosen-select").append($("<option />").val(datos[x]["fields"]["nombre"]).text(datos[x]["fields"]["nombre"]));
    	}
    	//console.log(typeof  paises);
	    localStorage.setItem('paises', JSON.stringify(paises));

	    $(".id_pais").chosen({width: "100%"});
<<<<<<< HEAD
	    $("#id_pais").remove();
	    $(".id_pais").next().attr("id", "id_pais") 	    
=======
	    $("#id_pais").remove(); 	    
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
	}
};

function loadProvincia(datos){
	var textSelect = $("#id_provincia option:selected").text();
	// en el editar esta el select comun
<<<<<<< HEAD
	if (textSelect == "---------" || $(".id_provincia").next() ) {
		//console.log(textSelect);
		
		var valSelect = $("#id_provincia option:selected").val();
		//console.log(valSelect);
		$("#id_provincia").parent().append(
			`<select data-placeholder="Seleccione una Provincia..." class="chosen-select id_provincia" tabindex="2">
            <option value=""></option>`);

		if ($(".id_provincia").next()){
			$(".id_provincia").parent().append(
			`<select data-placeholder="Seleccione una Provincia..." class="chosen-select id_provincia" tabindex="2">
            <option value=""></option>`);

			$(".id_provincia").next().remove();
		}

		var provincias = {};
		for (x in datos) {
    		//console.log(datos[x]["pk"]);
=======
	if (textSelect == "---------"){
		//
		//console.log(textSelect);
		var valSelect = $("#id_provincia option:selected").val();
		//console.log(valSelect);
		$("#id_provincia").parent().append(
			`<select data-placeholder="Elija una Provincia..." class="chosen-select id_provincia" tabindex="2">
            <option value=""></option>`);

		var provincias = {};
		for (x in datos) {
    		//console.log(datos[x]["pk"]);

>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
    		provincias[datos[x]["fields"]["nombre"]] = datos[x]["pk"];
    		$(".id_provincia").append($("<option />").val(datos[x]["fields"]["nombre"]).text(datos[x]["fields"]["nombre"]));
    	}
    	//console.log(typeof  paises);
	    localStorage.setItem('provincias', JSON.stringify(provincias));

	    $(".id_provincia").chosen({width: "100%"});
<<<<<<< HEAD
	    $("#id_provincia").remove();

	    try{
	    	var paisSelect = $("#id_pais");
	    	$(document).on('change', "#id_pais", function() {
	    		try{
	    			var paisText = $("a[class=chosen-single]")[0].text.replace(/\s/g, '');
			    } catch(error) {
		  			var paisText = "";
		  		}   	  
	    		if (!localStorage.getItem('pais_provincia')){
	    			localStorage.setItem('pais_provincia', paisText);
	    		} else {
	    			var paisTextSave = localStorage.getItem('pais_provincia');
	    			if (paisText == paisTextSave){
	    				return false;
	    			} else {
	    				localStorage.setItem('pais_provincia', paisText);
	    			}
	    		}
	    		
	    		var paisesList = JSON.parse(localStorage.getItem('paises'));
				//console.log(paisesList[paisText]);
				try{
					$.ajax({
					    type:"POST", 
					    url:"/provincias/", 
					    data:{value:paisesList[paisText], "csrfmiddlewaretoken": tok},
					    success:function(datos){ 
					    	//$(".id_provincia").next().remove();
					    	loadProvincia(datos);
					    },
					});
				} catch(error) {
		  			//console.log(error);
		  		}
			});	
	    } catch(error) {
  			//console.error(error);
  		}   	    
=======
	    $("#id_provincia").remove(); 	    
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
	}
};

function loadDerivacion(datos){
	var textSelect = $("#id_beneficiario option:selected").text();
	// en el editar esta el select comun
	if (textSelect == "---------"){
		//
		//console.log(textSelect);
		var valSelect = $("#id_beneficiario option:selected").val();
		//console.log(valSelect);
		$("#id_beneficiario").parent().append(
<<<<<<< HEAD
			`<select data-placeholder="Seleccione un Beneficiario..." class="chosen-select id_beneficiario" tabindex="2">
=======
			`<select data-placeholder="Elija un Beneficiario..." class="chosen-select id_beneficiario" tabindex="2">
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
            <option value=""></option>`);

		var beneficiario = {};
		for (x in datos) {
    		//console.log(datos[x]["pk"]);

    		beneficiario[datos[x]["fields"]["nombre"]] = datos[x]["pk"];
<<<<<<< HEAD
    		$(".id_beneficiario").append($("<option />").val(datos[x]["fields"]["nombre"]).text(datos[x]["fields"]["nombre"]+" "+datos[x]["fields"]["apellido"]));
=======
    		$(".id_beneficiario").append($("<option />").val(datos[x]["fields"]["nombre"]).text(datos[x]["fields"]["nombre"]));
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
    	}
    	//console.log(typeof  paises);
	    localStorage.setItem('beneficiario', JSON.stringify(beneficiario));

	    $(".id_beneficiario").chosen({width: "100%"});
	    $("#id_beneficiario").remove(); 	    
	}
};

function loadPrestador(datos){
	var textSelect = $("#id_prestador option:selected").text();
	// en el editar esta el select comun
	if (textSelect == "---------"){
		//
		//console.log(textSelect);
		var valSelect = $("#id_prestador option:selected").val();
		//console.log(valSelect);
		$("#id_prestador").parent().append(
<<<<<<< HEAD
			`<select data-placeholder="Seleccione un Prestador..." class="chosen-select id_prestador" tabindex="2">
            <option value=""></option>`);

		$("#id_prestador").parent().append(
			`<a href="/prestador/" title="Agregar Prestador" style="float:right">
	          <span class="glyphicon glyphicon-plus" id="icon_prestador"></span>
	        </a>`);

		var prestador = {};
		for (x in datos) {
    		prestador[datos[x]["fields"]["nombre"]] = datos[x]["pk"];
    		$(".id_prestador").append($("<option />").val(datos[x]["fields"]["nombre"]).text(datos[x]["fields"]["nombre"]));
    	}
=======
			`<select data-placeholder="Elija un Prestador..." class="chosen-select id_prestador" tabindex="2">
            <option value=""></option>`);

		var prestador = {};
		for (x in datos) {
    		//console.log(datos[x]["pk"]);

    		prestador[datos[x]["fields"]["nombre"]] = datos[x]["pk"];
    		$(".id_prestador").append($("<option />").val(datos[x]["fields"]["nombre"]).text(datos[x]["fields"]["nombre"]));
    	}
    	//console.log(typeof  paises);
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
	    localStorage.setItem('prestador', JSON.stringify(prestador));

	    $(".id_prestador").chosen({width: "100%"});
	    $("#id_prestador").remove(); 	    
	}
<<<<<<< HEAD

	try{	
    	var paisSelect = $("#id_prestador");
    	$(document).on('change', paisSelect, function() {
    		try{
    			var paisText = $("a[class=chosen-single]")[0].text.replace(/\s/g, '');
    			//alert(paisText);
		    } catch(error) {
	  			var paisText = "";
	  		}   	  
    		if (!localStorage.getItem('prestador')){
    			//
    		} else {
    			var paisTextSave = localStorage.getItem('prestador');
    			if (paisText == paisTextSave){
    				return false;
    			} 
    		}
    		try{
	    		var paisesList = JSON.parse(localStorage.getItem('prestador'));
				//console.log(paisesList[paisText]);
			} catch(error) {
	  			//console.log(error);
	  		};
	  		try{
				$.ajax({
				    type:"POST", 
				    url:"/prestador/get/", 
				    data:{value:paisesList[paisText], "csrfmiddlewaretoken": tok},
				    success:function(datos){ 
				    	//$(".id_provincia").next().remove();
				    	$("#nombre_prestador").val(datos[0]["fields"]["nombre"]);
				    	$("#apellido_prestador").val(datos[0]["fields"]["apellido"]);
				    	$("#documento_prestador").val(datos[0]["fields"]["documento"]);
				    	$("#matricula_prestador").val(datos[0]["fields"]["matricula"]);
				    	//console.log(datos[0]["fields"]["apellido"]);
				    },
				    error:function(e){
				    	//
				    }
				});
			} catch(error) {
	  			//console.log(error);
	  		};
		});

	} catch(error) {
  		//console.error(error);
  	}   	    
};

function loadPrestacion(datos){
	var textSelect = $("#id_prestacion option:selected").text();
	// en el editar esta el select comun
	if (textSelect == "---------"){
		//
		//console.log(textSelect);
		var valSelect = $("#id_prestacion option:selected").val();
		//console.log(valSelect);
		$("#id_prestacion").parent().append(
			`<select data-placeholder="Seleccione un Prestador..." class="chosen-select id_prestacion" tabindex="2">
            <option value=""></option>`);

		var prestacion = {};
		for (x in datos) {
    		//console.log(datos[x]["pk"]);

    		prestacion[datos[x]["fields"]["nombre"]] = datos[x]["pk"];
    		$(".id_prestacion").append($("<option />").val(datos[x]["fields"]["nombre"]).text(datos[x]["fields"]["nombre"]));
    	}
    	//console.log(typeof  paises);
	    localStorage.setItem('prestacion', JSON.stringify(prestacion));

	    $(".id_prestacion").chosen({width: "100%"});
	    $("#id_prestacion").remove(); 	    
	}
};
=======
};

>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf

function loadBeneficiarioNotificacion(datos){
	var textSelect = $("#id_beneficiario option:selected").text();
	// en el editar esta el select comun
	if (textSelect == "---------"){
		//
		//console.log(textSelect);
		var valSelect = $("#id_beneficiario option:selected").val();
		//console.log(valSelect);
		$("#id_beneficiario").parent().append(
<<<<<<< HEAD
			`<select data-placeholder="Seleccione un Beneficiario..." class="chosen-select id_beneficiario" tabindex="2">
            <option value=""></option>`);
		$("#id_beneficiario").parent().append(
			`<a href="/beneficiario/" title="Agregar Beneficiario" style="float:right">
	          <span class="glyphicon glyphicon-plus" id="icon_beneficiario"></span>
	        </a>`);
=======
			`<select data-placeholder="Elija un Beneficiario..." class="chosen-select id_beneficiario" tabindex="2">
            <option value=""></option>`);
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf

		var beneficiario = {};
		for (x in datos) {
    		//console.log(datos[x]["pk"]);

    		beneficiario[datos[x]["fields"]["nombre"]] = datos[x]["pk"];
    		$(".id_beneficiario").append($("<option />").val(datos[x]["fields"]["nombre"]).text(datos[x]["fields"]["nombre"]));
    	}

	    localStorage.setItem('beneficiario2', JSON.stringify(beneficiario));

	    $(".id_beneficiario").chosen({width: "100%"});
	    $("#id_beneficiario").remove(); 	    
	}
<<<<<<< HEAD

	try{	
    	var paisSelect = $("#id_beneficiario");
    	$(document).on('change', paisSelect, function() {
    		try{
    			var paisText = $("a[class=chosen-single]")[0].text.replace(/\s/g, '');
    			//alert(paisText);
		    } catch(error) {
	  			var paisText = "";
	  		}   	  
    		if (!localStorage.getItem('beneficiario2')){
    			//
    		} else {
    			var paisTextSave = localStorage.getItem('beneficiario2');
    			if (paisText == paisTextSave){
    				return false;
    			} 
    		}
    		try{
    			var paisesList = JSON.parse(localStorage.getItem('beneficiario2'));
    			textBeneficiario = $("a[class=chosen-single]")[1].text.replace(/\s/g, '');
    		} catch(error) {
    			//console.log(error);
    		};
			//console.log(paisesList[textBeneficiario]);
			try{
				$.ajax({
				    type:"POST", 
				    url:"/beneficiario/get/", 
				    data:{value:paisesList[textBeneficiario], "csrfmiddlewaretoken": tok},
				    success:function(datos){ 
				    	//$(".id_provincia").next().remove();
				    	$("#nombre_beneficiario").val(datos[0]["fields"]["nombre"]);
				    	$("#apellido_beneficiario").val(datos[0]["fields"]["apellido"]);
				    	$("#documento_beneficiario").val(datos[0]["fields"]["documento"]);
				    	//console.log(datos[0]["fields"]["apellido"]);
				    },
				}).fail( function( jqXHR, textStatus, errorThrown ) {
				    //console.log(errorThrown);
				});
			} catch(error) {
    			//console.log(error);
    		};
		});
	} catch(error) {
  		//console.error(error);
  	}   	    
};

=======
};
>>>>>>> 02b502ce1adfefad03404a1a33289efcdad2fbaf
