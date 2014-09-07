$(document).ready(function() {
	$('.login-window').click(function(){
		console.log('test');
		if($('.ui-dialog').css('display') === 'block'){
			$('#login_form').dialog('close');
		}

		else{
			$('#login_form').dialog({modal: true});
		}

	});
});