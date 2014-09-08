$(document).ready(function(){
	$("#register_form").validate({
	rules:{
		username: {
			required: true,
			minlength: 6,
			remote: {
				url: '/register/',
				type: 'get',
				data: {
					username: function() {
						return $( "#id_username" ).val();
					}
				},
				dataType: 'json'
			}
		},
		email: {
			required: true,
			email: true,
			remote: {
				url: '/register/',
				type: 'get',
				data: {
					email: function() {
						return $( "#id_email" ).val();
					}
				},
				dataType: 'json'
			}	
		},
		password1:{
			required: true,
			minlength: 6
		},
		password2:{
			required: true,
			minlength: 6,
			equalTo: "#id_password1"
		},
		first_name: "required",
		middle_initial: "required",
		last_name: "required",
		birth_date: {
			required: true,
			dateISO: true
		},
		street_address:"required",
		city: "required",
		state: "required",
		zip_code: {
			required: true,
			digits: true,
		}
	},
	messages: {
		username: {
			remote: $.validator.format("{0} is already in use.")
		},
		email: {
			remote: $.validator.format("{0} is already in use.")
		}
	},
	debug: false,
	validClass: "form_success",
	errorClass: "form_error",
	errorPlacement: function(error, element) {
		error.appendTo( element.next(".error_container"));
	}
	});
	
});
