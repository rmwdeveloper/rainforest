$(document).ready(function(){
	/* When user clicks on the mobile_search_icon
	(the magnifying glass) in the navbar the search bar
	slides into view under the navbar */ 
	var mobile_search_icon = $('#header_search_button a');
	var search_input = $('input[type="search"]');
	var header = $('header');
	var toggled = false;
	mobile_search_icon.click(function() {
		if(toggled==false){
			header.after(search_input);
			search_input.toggleClass('toggle_search')
			toggled = true
		}
	});

});