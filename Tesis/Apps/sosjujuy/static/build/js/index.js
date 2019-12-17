var paises = new Array();

$( document ).ready(function() {
    var tok = $('input[name=csrfmiddlewaretoken]').attr("value");
    console.log(tok);

    $( "#beneficiarioForm" ).submit(function( event ) {
    	var text = $("a[class=chosen-single]").find("span")[0].innerText;
    	
	  	var paisesList = JSON.parse(localStorage.getItem('paises'));
	  	
	  	$("<input />").attr("type", "hidden")
          .attr("name", "pais")
          .attr("value", paisesList[text])
          .attr("id", "pais")
          .attr("data", text)
          .appendTo("#beneficiarioForm");
	});	

    $.ajax({
	    type:"POST", 
	    url:"/search/", 
	    data:{url:"Z562316", "csrfmiddlewaretoken": tok},
	    success:function(datos){ 
	    	loadData(datos);
	    },
	});
});

function loadData(datos){

	var textSelect = $("#id_pais option:selected").text();
	// en el editar esta el select comun
	if (textSelect != "---------"){
		//
	} else {
		console.log(textSelect);
		var valSelect = $("#id_pais option:selected").val();
		console.log(valSelect);
		$("#id_pais").parent().append(
			`<select data-placeholder="Elija un País..." class="chosen-select" tabindex="2">
            <option value=""></option>`);

		var paises = {};
		for (x in datos) {
    		console.log(datos[x]["pk"]);

    		paises[datos[x]["fields"]["nombre"]] = datos[x]["pk"];
    		$(".chosen-select").append($("<option />").val(datos[x]["fields"]["nombre"]).text(datos[x]["fields"]["nombre"]));
    	}

    	//console.log(typeof  paises);
	    localStorage.setItem('paises', JSON.stringify(paises));

	    $(".chosen-select").chosen({width: "100%"});
	    $("#id_pais").remove(); 	    
	}
};