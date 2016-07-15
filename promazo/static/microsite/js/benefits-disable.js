$(document).ready(function(){	
	$('link[href="student.css"]').attr('disabled', 'disabled');	
	$('a#student p.other').click(function(e){
		e.preventDefault();											 
		$('link[href="student.css"]').removeAttr('disabled');
		$('link[href="company.css"]').attr('disabled', 'disabled');		
	});
	$('a#company p.other').click(function(e){
		e.preventDefault();											 
		$('link[href="company.css"]').removeAttr('disabled');
		$('link[href="student.css"]').attr('disabled', 'disabled');	
	});
});