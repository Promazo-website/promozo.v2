(document).ready(function(){
	$('ul.navbar li:nth-child(4)').mouseover(function(){
//		$(this).animate({opacity:0},200);
		$('ul.navbar li:nth-child(2)').animate({opacity:1},200);
		$('ul.navbar li:nth-child(3)').animate({opacity:1},200);
	});
	$('nav#how-page ul.navbar').mouseleave(function(){
		$('nav#how-page ul.navbar li:nth-child(2)').animate({opacity:0},200);
		$('nav#how-page ul.navbar li:nth-child(3)').animate({opacity:0},200);
	});
});