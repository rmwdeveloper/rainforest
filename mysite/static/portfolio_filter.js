$(document).ready(function() {
	$('#filter_projects button').click(function(event){
		event.preventDefault();
		var form_inputs = new Array();
		$('#filter_projects *').filter('option:selected').each(function(){
			
			if ((form_inputs.indexOf(this.value) == -1) && this.value !==''){
				form_inputs.push(this.value);	
			}	
		});
		
		form_inputs_object = $.extend({}, form_inputs);
		
		$.ajax({
			url : '',
			type: 'get',
			// data: form_inputs_object,
			data: {
					
					form_inputs: JSON.stringify(form_inputs),
				},
			dataType: 'JSON',
			success: function(data) {
				console.log(data[0]);

			}
		});

		// request.done(function (response, textStatus, jqXHR) {
		// 	console.log(jqXHR);
		// })
	});
});