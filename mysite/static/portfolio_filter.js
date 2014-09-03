$(document).ready(function() {

	$('.chosen-select').chosen({
		width: '100%',
	});
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
			data: {
					
					form_inputs: JSON.stringify(form_inputs),
				},
			dataType: 'JSON',
			success: function(data) {
				$('#sortable li').show();
				if (data.length > 0){
					$('#sortable li').hide();

					for(var i=0; i<data.length ; i++){
						$('#'+data[i]).show();
					}
				}

			}
		});
	});
});