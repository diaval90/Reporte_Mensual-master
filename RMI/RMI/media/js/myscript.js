$(document).ready(function() {
	    	$(".button-collapse").sideNav();	    		    	
			$(".dropdown-button").dropdown({
				inDuration: 300,
				outDuration: 225,
				constrain_with: false,
				hover: true,
				gutter: 0,
				belowOrigin: false,
				aligment: 'left'
			}
			);	
			$('select').material_select();
	    	$('.modal-trigger').leanModal();
	    	$('.slider').slider({
	    		
	    		height:525
	    	});	 		
			$('.parallax').parallax();
    });
        
			