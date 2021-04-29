$(document).ready(function(){
	// Init
		carouselInit();
	// ---------------------------------------------------------------------------


	$('.carousel').on('click', '.btn-control, .preview', function(){
		//Set variables
		var count = parseInt($(this).parents('.carousel').attr('data-count'));
		var current = parseInt($(this).parents('.carousel').attr('data-current'));


		if( $(this).attr('data-direction') == 'right' ){
			if( current + 1 > count ) { var marker = 1; }
			else{ var marker = current + 1; }
		}
		else {
			if( current - 1 == 0 ) { var marker = count; }
			else{ var marker = current - 1; }
		}


		if(current < marker) {
			// Move to right
				$(this).parents('.carousel').find('.items .item[data-marker="'+current+'"]').removeClass('center').removeClass('center-left').removeClass('center-right').removeClass('right-center').removeClass('left-center').addClass('center-left');
				$(this).parents('.carousel').find('.items .item[data-marker="'+marker+'"]').removeClass('center').removeClass('center-left').removeClass('center-right').removeClass('right-center').removeClass('left-center').addClass('right-center');
			//-----------------------------------------------
		}
		else{
			// Move to left
				$(this).parents('.carousel').find('.items .item[data-marker="'+current+'"]').removeClass('center').removeClass('center-left').removeClass('center-right').removeClass('right-center').removeClass('left-center').addClass('center-right');
				$(this).parents('.carousel').find('.items .item[data-marker="'+marker+'"]').removeClass('center').removeClass('center-left').removeClass('center-right').removeClass('right-center').removeClass('left-center').addClass('left-center');
			//-----------------------------------------------
		}

		//Set data
		$(this).parents('.carousel').attr('data-current', marker);


		//Set markers
		carouselInit();
		$(this).parents('.carousel').find('.markers > li').removeClass('active');
		$(this).parents('.carousel').find('.markers > li[data-marker="'+marker+'"]').addClass('active');
	});


	// Marker Click
	$('.carousel').on('click', '.markers li', function(){
		//Set variables
		var current = parseInt($(this).parents('.carousel').attr('data-current'));
		var marker = parseInt($(this).attr('data-marker'));

		if(current < marker) {
			// Move to right
				$(this).parents('.carousel').find('.items .item[data-marker="'+current+'"]').removeClass('center').removeClass('center-left').removeClass('center-right').removeClass('right-center').removeClass('left-center').addClass('center-left');
				$(this).parents('.carousel').find('.items .item[data-marker="'+marker+'"]').removeClass('center').removeClass('center-left').removeClass('center-right').removeClass('right-center').removeClass('left-center').addClass('right-center');
			//-----------------------------------------------
		}
		else{
			// Move to left
				$(this).parents('.carousel').find('.items .item[data-marker="'+current+'"]').removeClass('center').removeClass('center-left').removeClass('center-right').removeClass('right-center').removeClass('left-center').addClass('center-right');
				$(this).parents('.carousel').find('.items .item[data-marker="'+marker+'"]').removeClass('center').removeClass('center-left').removeClass('center-right').removeClass('right-center').removeClass('left-center').addClass('left-center');
			//-----------------------------------------------
		}
			
		//Set data
		$(this).parents('.carousel').attr('data-current', marker);


		//Set markers
		carouselInit();
		$(this).parents('.carousel').find('.markers > li').removeClass('active');
		$(this).parents('.carousel').find('.markers > li[data-marker="'+marker+'"]').addClass('active');
	});

	//Swipe
		//Swipe function
			$(function() {
				if( $( window ).width() < 1000 ) {
					//Click
						$(".carousel").swipe( { fingers:'all', swipeStatus:swipePartners, allowPageScroll:"vertical"} );
						
						function swipePartners(event, phase, direction, distance) {
							if( phase == 'start' || phase == 'move' ){
								//console.log( phase +" you have swiped " + distance + "px in direction:" + direction );

								//Set offset-------------------------------------
								if( phase == 'move' ){
									if( direction == 'left' && distance>=100 ) { 
										$(this).find('.btn-control[data-direction="right"]').trigger('click');
										return false; }

									else if( direction == 'right' && distance>=100 ) {
										$(this).find('.btn-control[data-direction="left"]').trigger('click');
										return false; }
								}
							}
						}
					//Click
				}
			});
		//Swipe function
//Swipe
});


function carouselInit() {

	$('body').find('.carousel').each(function(index){
		if( parseInt($(this).attr('data-count')) >= 3 ){
			var count = parseInt($(this).attr('data-count'));
			var current = parseInt($(this).attr('data-current'));


			if( current + 1 > count ) { var next = 1; }
			else{ var next = current + 1; }
			if( current - 1 == 0 ) { var prev = count; }
			else{ var prev = current - 1; }


			var nextimagesrc = $(this).find('.item[data-marker="'+next+'"] img').attr('src');
			var previmagesrc = $(this).find('.item[data-marker="'+prev+'"] img').attr('src');

			$(this).find('.preview[data-direction="right"]').css({
				'background': 'url('+nextimagesrc+') no-repeat center center scroll', 
				'-webkit-background-size': 'cover',
				'-moz-background-size': 'cover',
				'-o-background-size': 'cover',
				'background-size': 'cover'
			});

			$(this).find('.preview[data-direction="left"]').css({
				'background': 'url('+previmagesrc+') no-repeat center center scroll',
				'-webkit-background-size': 'cover',
				'-moz-background-size': 'cover',
				'-o-background-size': 'cover',
				'background-size': 'cover'
			});

			var color = $(this).find('.markers > li.active').attr('data-style');

			if( color == 'dark' ) {
				$(this).addClass('dark');
			}
			else {
				$(this).removeClass('dark');
			}

		}
	});

}// .carouselInit