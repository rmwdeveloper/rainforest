$(document).ready(function() {
	$('.login-window').click(function(){

		if($('.ui-dialog').css('display') === 'block'){
			$('#login_form').dialog('close');
		}
		
		else{
			$('#login_form').dialog();
		}

	});
});