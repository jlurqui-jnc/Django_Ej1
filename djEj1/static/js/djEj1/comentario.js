(function() {

	$("#btn_comentario").off("click")
	$("#btn_comentario" ).click(function(event) {

		event.preventDefault();
		
		var vUrl = '/creacomentario/' + $('#formcmt').find('input[name="noticia"]' ).val();
		var vForm = {
			'fecha' : $('#formcmt').find('input[name="fecha"]' ).val(),
			'noticia' : $('#formcmt').find('input[name="noticia"]').val(),
			'texto' : $('#formcmt').find('textarea[name="texto"]').val(),
			'usuario' : $('#formcmt').find('select[name="usuario"]').val()				
		};
			
		$.ajax({
		    url: vUrl ,
		    type: "POST",
		    data: vForm,
		    error: function(jqXHR, textStatus, errorThrown ) {
		    	alert(errorThrown);
		    },
		    success: function (data) {
		       $('#listacomentarios').append('<li><p>' + vForm.texto + '</p></li>');			       
		    }
		});
			
	});
	
})();