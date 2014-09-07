$(document).ready(function() {
	$('#filter_projects_form_toggle > .fa-angle-double-down').hide();
	
	$('#filter_projects_form_toggle').click(function(event){
		
		var filter_projects_form = $('form#filter_projects');
		var up_arrow = $('#filter_projects_form_toggle > .fa-angle-double-up')
		var down_arrow = $('#filter_projects_form_toggle > .fa-angle-double-down')
		
		
		if(filter_projects_form.css('display') === 'none'){
			up_arrow.show();
			down_arrow.hide();
		}
		if(filter_projects_form.css('display') === 'block'){
			
			down_arrow.show();
			up_arrow.hide();
		}
		filter_projects_form.slideToggle();
	});

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
				$('.project-container').show();
				if (data.length > 0){
					$('.project-container').hide();

					for(var i=0; i<data.length ; i++){
						$('#'+data[i]).show();
					}
				}

			}
		});
	});
});