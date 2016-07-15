$(document).ready(function(){
//	$('ul.bxslider li div').animate({opacity:0},3000);
	$('ul.bxslider a').click(function(e){
		e.preventDefault();
	});
	$('ul.bxslider li p.expand').mouseover(function(){
		$('ul.bxslider li div').animate({opacity:1},400);	
	}).mouseleave(function(){
		$('ul.bxslider li div').animate({opacity:0},400);		
	});
});



$(document).ready(function(){
	var overlayHeight =	$('ul.bxslider img').height();
	var overlayWidth =	$('ul.bxslider img').width();	
	$('div.overlay').css('height',overlayHeight);
	$('div.overlay').css('width',overlayWidth);	
});

$(document).ready(function(){
	$('p.link').mouseover(function(){
		$(this).animate({width:'+=30px'},300);
	}).mouseleave(function(){
		$(this).animate({width:'-=30px'},300);
	});
});

$(document).ready(function(){
	$('section.projects ul.project-items h4').click(function(e){
		e.preventDefault();
	});
});

$(document).ready(function(){
	$('section.projects ul.project-items li:nth-child(1) h4').click(function(){
		$(this).css('background','#CCC');
		$('section.projects ul.project-items li:nth-child(2) h4').css('background','#EEE');
		$('section.projects ul.project-items li:nth-child(3) h4').css('background','#EEE');			
		$('section.projects ul.alternates > li:nth-child(1)').css('display','none');		
		$('section.projects ul.alternates li.one-image#support').css('display','block');	
		$('section.projects ul.alternates li.one-image#exploratory').css('display','none');	
		$('section.projects ul.alternates li.one-image#just-in-time').css('display','none');
		$('p.overlay').css('background','#10811F');
	});
	$('section.projects ul.project-items li:nth-child(2) h4').click(function(){
		$(this).css('background','#CCC');					
		$('section.projects ul.project-items li:nth-child(1) h4').css('background','#EEE');
		$('section.projects ul.project-items li:nth-child(3) h4').css('background','#EEE');				
		$('section.projects ul.alternates > li:nth-child(1)').css('display','none');		
		$('section.projects ul.alternates li.one-image#support').css('display','none');	
		$('section.projects ul.alternates li.one-image#exploratory').css('display','block');	
		$('section.projects ul.alternates li.one-image#just-in-time').css('display','none');	
		$('p.overlay').css('background','#C9303A');		
	});
	$('section.projects ul.project-items li:nth-child(3) h4').click(function(){
		$(this).css('background','#CCC');
		$('section.projects ul.project-items li:nth-child(1) h4').css('background','#EEE');
		$('section.projects ul.project-items li:nth-child(2) h4').css('background','#EEE');		
		$('section.projects ul.alternates > li:nth-child(1)').css('display','none');		
		$('section.projects ul.alternates li.one-image#support').css('display','none');	
		$('section.projects ul.alternates li.one-image#exploratory').css('display','none');	
		$('section.projects ul.alternates li.one-image#just-in-time').css('display','block');	
		$('p.overlay').css('background','#2534B4');		
	});	
});

/*
// Hover-reveal for types of projects or promazo paths
$(document).ready(function(){
	var list = '.projects3 .proj-reveal';
	$(list).each(function(){
		$(this).mouseover(function(){
			if ($(this).find('i').css('opacity') == 1) {
				$(this).find('i').animate({opacity:0},300);
				$(this).find('p').animate({opacity:0},300);
				$(this).find('ul').animate({opacity:1},300);
				$(this).find('h3').animate({marginTop:'-100px'},300);
			}
		}).mouseleave(function(){
			if ($(this).find('i').css('opacity') == 0) {
				$(this).find('i').animate({opacity:1},300);
				$(this).find('p').animate({opacity:1},300);
				$(this).find('ul').animate({opacity:0},300);
				$(this).find('h3').animate({marginTop:0},300);
			}
		});
	});
});
*/

// Random selection of desk drawing for homepage
$(document).ready(function() {
  var urls = ['1', '2', '3', '4', '5', '6'];
  var ranDesk = 'pm-desk-' + urls[Math.round(Math.random() * urls.length)] + '.png';
  if (ranDesk == 'pm-desk-undefined.png') {
    function swap() {
      document.getElementById('random-desk').setAttribute('src', '/static/microsite/images/sketches-png/pm-desk-student.png');
    }
  } else {
    function swap() {
      document.getElementById('random-desk').setAttribute('src', '/static/microsite/images/sketches-png/' + ranDesk);
    }
  }

  // Mozilla, Opera and webkit nightlies currently support this event
  if ( document.addEventListener ) {
    window.addEventListener( 'load', swap, false );
  // If IE event model is used
  } else if ( document.attachEvent ) {
    window.attachEvent( 'onload', swap );
  }
})();