$(document).ready(
function() {
    $('#countries').dataTable();
    $('.ajax_link').click(function(){
	
	$.get('/test', function(data) {
	    alert(data);
	});
    })
});