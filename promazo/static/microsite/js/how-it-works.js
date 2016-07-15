/*
$(document).ready(function(){
	$('section.benefits ul li img').mouseover(function(){
		$(this).animate({width:'+=10px'},200);
	});	
	$('section.benefits ul li img').mouseleave(function(){
		$(this).animate({width:'-=10px'},200);
	});		
});
*/

/*
$(document).ready(function(){
	var scrollPositionHow =
	$('p#introducing').offset().top;
	$('.down-arrow').click(function(e){
		e.preventDefault();
		$('html, body').animate({scrollTop:scrollPositionHow}, 500);
	});
});	
*/


// Click-reveal for Company/Student Benefits
$(document).ready(function(){
/*	$('section.benefits ul.benefits-list > li:nth-child(1)').mouseover(function(){
		if ($('section.benefits ul.benefits-list > li:nth-child(1) ul.more-info').css('opacity')==0) {																			
			$('section.benefits img').animate({marginTop:'-=10px'},200);
		}
	}).mouseleave(function(){
		if ($('section.benefits ul.benefits-list > li:nth-child(1) ul.more-info').css('opacity')==0) {																			
			$('section.benefits img').animate({marginTop:'+=10px'},200);
		}
	});*/
   $('.benefits #sben-skills').click(function(){
		if ($('.benefits #sben-skills ul.more-info').css('opacity')==0) {
//			$('.benefits #sben-skills ul.more-info').animate({marginTop:'+=40px'},0);
			$('.benefits #sben-skills ul.more-info').animate({opacity:1},200);
			$('.benefits #sben-skills h3').animate({opacity:0},200);
			$('.benefits #sben-skills i').animate({fontSize:'60px'},200);
		} else {		
			$('.benefits #sben-skills ul.more-info').animate({opacity:0},100);
//			$('.benefits #sben-skills ul.more-info').animate({marginTop:'-=40px'},0);
			$('.benefits #sben-skills h3').animate({opacity:1},200);
			$('.benefits #sben-skills i').animate({fontSize:'120px'},200);
		}
	});
	$('.benefits #sben-passions').click(function(){
		if ($('.benefits #sben-passions ul.more-info').css('opacity')==0) {
//			$('.benefits #sben-passions ul.more-info').animate({marginTop:'+=40px'},0);
			$('.benefits #sben-passions ul.more-info').animate({opacity:1},200);
			$('.benefits #sben-passions h3').animate({opacity:0},200);
			$('.benefits #sben-passions i').animate({fontSize:'60px'},200);
		} else {
			$('.benefits #sben-passions ul.more-info').animate({opacity:0},100);
//			$('.benefits #sben-passions ul.more-info').animate({marginTop:'-=40px'},0);
			$('.benefits #sben-passions h3').animate({opacity:1},200);
			$('.benefits #sben-passions i').animate({fontSize:'120px'},200);
		}
	});
	$('.benefits #sben-connections').click(function(){
		if ($('.benefits #sben-connections ul.more-info').css('opacity')==0) {
//			$('.benefits #sben-connections ul.more-info').animate({marginTop:'+=40px'},0);
			$('.benefits #sben-connections ul.more-info').animate({opacity:1},200);
			$('.benefits #sben-connections h3').animate({opacity:0},200);
			$('.benefits #sben-connections i').animate({fontSize:'60px'},200);
		} else {
			$('.benefits #sben-connections ul.more-info').animate({opacity:0},100);
//			$('.benefits #sben-connections ul.more-info').animate({marginTop:'-=40px'},0);
			$('.benefits #sben-connections h3').animate({opacity:1},200);
			$('.benefits #sben-connections i').animate({fontSize:'120px'},200);
		}
	});
	$('.benefits #sben-paid').click(function(){
		if ($('.benefits #sben-paid ul.more-info').css('opacity')==0) {
//			$('.benefits #sben-paid ul.more-info').animate({marginTop:'+=40px'},0);
			$('.benefits #sben-paid ul.more-info').animate({opacity:1},200);
			$('.benefits #sben-paid h3').animate({opacity:0},200);
			$('.benefits #sben-paid i').animate({fontSize:'60px'},200);
		} else {
			$('.benefits #sben-paid ul.more-info').animate({opacity:0},100);
//			$('.benefits #sben-paid ul.more-info').animate({marginTop:'-=40px'},0);
			$('.benefits #sben-paid h3').animate({opacity:1},200);
			$('.benefits #sben-paid i').animate({fontSize:'120px'},200);
		}
	});
    /*
	$('.benefits a').click(function(e){
		e.preventDefault();
		$('.benefits ul.more-info').animate({opacity:0},0);
		$('.benefits ul.more-info').animate({marginTop:'-100px'},0);
		$('.benefits h3').animate({opacity:1},0);
		$('.benefits i').animate({fontSize:'120px'},0);
	});
	*/
	/*
	$('section.benefits ul.benefits-list li:nth-child(1)').mouseleave(function(){
		$('section.benefits ul.benefits-list li:nth-child(1) ul.more-info').animate({opacity:0, marginTop:'+=50px'},200);
		$('section.benefits ul.benefits-list li:nth-child(1) h3').animate({opacity:1},200);	
		$('section.benefits ul.benefits-list li:nth-child(1) img').animate({width:'+=50px'},200);		
	});	
	*/
});


// Click-reveal for Company/Student Benefits
$(document).ready(function(){
   $('.projects3 #proj-support').click(function(){
		if ($('.projects3 #proj-support ul.more-info').css('opacity')==0) {
			$('.projects3 #proj-support ul.more-info').animate({opacity:1},200);
//			$('.projects3 #proj-support h3').animate({opacity:0},200);
			$('.projects3 #proj-support p').animate({opacity:0},200);
			$('.projects3 #proj-support i').animate({fontSize:'60px'},200);
		} else {
			$('.projects3 #proj-support ul.more-info').animate({opacity:0},100);
//			$('.projects3 #proj-support h3').animate({opacity:1},200);
			$('.projects3 #proj-support p').animate({opacity:1},200);
			$('.projects3 #proj-support i').animate({fontSize:'120px'},200);
		}
	});
	$('.projects3 #proj-exploratory').click(function(){
		if ($('.projects3 #proj-exploratory ul.more-info').css('opacity')==0) {
			$('.projects3 #proj-exploratory ul.more-info').animate({opacity:1},200);
//			$('.projects3 #proj-exploratory h3').animate({opacity:0},200);
			$('.projects3 #proj-exploratory p').animate({opacity:0},200);
			$('.projects3 #proj-exploratory i').animate({fontSize:'60px'},200);
		} else {
			$('.projects3 #proj-exploratory ul.more-info').animate({opacity:0},100);
//			$('.projects3 #proj-exploratory h3').animate({opacity:1},200);
			$('.projects3 #proj-exploratory p').animate({opacity:1},200);
			$('.projects3 #proj-exploratory i').animate({fontSize:'120px'},200);
		}
	});
	$('.projects3 #proj-immediate').click(function(){
		if ($('.projects3 #proj-immediate ul.more-info').css('opacity')==0) {
			$('.projects3 #proj-immediate ul.more-info').animate({opacity:1},200);
//			$('.projects3 #proj-immediate h3').animate({opacity:0},200);
			$('.projects3 #proj-immediate p').animate({opacity:0},200);
			$('.projects3 #proj-immediate i').animate({fontSize:'60px'},200);
		} else {
			$('.projects3 #proj-immediate ul.more-info').animate({opacity:0},100);
//			$('.projects3 #proj-immediate h3').animate({opacity:1},200);
			$('.projects3 #proj-immediate p').animate({opacity:1},200);
			$('.projects3 #proj-immediate i').animate({fontSize:'120px'},200);
		}
	});
});





