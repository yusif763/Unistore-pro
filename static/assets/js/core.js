$(document).ready(function(){
	
	iconInit();

	// Init cart
		setTimeout(function(){
			$('.cart').css({
				'opacity':'1'
			});
		},2000);
	// Init cart

	// Init bars
		$('.bars .bar').each(function(index){
			$(this).css({
				'background': 'url('+$(this).attr('data-background')+') no-repeat center center scroll',
				'-webkit-background-size': 'cover',
				'-moz-background-size': 'cover',
				'-o-background-size': 'cover',
				'background-size': 'cover'
			});
		});
	// Init bars

	//Navbar
		if( $('body').find('.navbar-buy').length > 0 ){
			$(window).scroll(function () {
				if(  $(window).scrollTop() > 300 ){
					$('body').find('.navbar-buy').fadeIn('slow');
				}
				else{
					$('body').find('.navbar-buy').fadeOut('fast');
				}
			});
		}

		// Search
			$('.navbar').on('click', '.search .input button', function(){
				console.log( $(this).parents('.search').attr('data-style') );

				if( $(this).parents('.search').attr('data-style') == 'hidden' ){ $(this).parents('.search').attr('data-style', 'visible'); }
				else { $(this).parents('.search').attr('data-style', 'hidden'); }
			});
		// .......................................................
	//Navbar

	//Footer
		$('footer').on('click', '.menu h1', function(){
			if( $(window).width() < 768 ){
				if( $(this).parent().find('.list-group').css('display') == 'none' ){
					$(this).find('i').addClass('open');
					$(this).parent().find('.list-group').slideDown('slow');
				}
				else{
					$(this).find('i').removeClass('open');
					$(this).parent().find('.list-group').slideUp('slow');
				}
			}
		});
	//Footer

	//Scroll
		$('a.scroll-to').click(function(){
		    $('html, body').animate({
		        scrollTop: $( $.attr(this, 'href') ).offset().top
		    }, 500);
		    return false;
		});
	//Scroll

	//Forms
		$('.group-select').on('click', 'input.select, .arrow, a', function() {
			if( $(this).parent().attr('data-toggle') == 'open' ) {
				$(this).parent().attr('data-toggle','close');
				$(this).parent().find('ul.dropdown').slideUp('fast'); }
			else{
				$(this).parent().focus();
				$(this).parent().attr('data-toggle','open');
				$(this).parent().find('ul.dropdown').slideDown('fast'); }
		});

		$('.group-select').on('click', 'ul.dropdown > li', function() {
			
			var value = $(this).attr('data-value');

			$(this).parents('.group-select').find('input.select').val(value);

			$(this).parents('.group-select').attr('data-toggle','close');
			$(this).parents('.group-select').find('ul.dropdown').slideUp('fast');

		});

		$('.group-select').focusout(function() {
			$(this).attr('data-toggle','close');
			$(this).find('ul.dropdown').slideUp('fast');
		});
	//Forms

	//Modal Sign In
		$('body').on('click', '*[data-action="Sign-In"]', function(){
			$('#Modal-ForgotPassword').modal('hide');
			setTimeout(function(){ $('#Modal-SignIn').modal('show'); }, 600);
		});

		$('body').on('click', '*[data-action="Forgot-Password"]', function(){
			$('#Modal-SignIn').modal('hide');
			setTimeout(function(){ $('#Modal-ForgotPassword').modal('show'); }, 600);
		});
	//Modal Sign In

	//Modal Gallery
		//Init
			if( $('body').find('.container.gallery').length > 0 ){

				$('.container.gallery .preview').each(function(index){
					console.log( $(this).attr('data-preview') );

					$(this).css({
						'background': 'url('+$(this).attr('data-preview')+') no-repeat center center scroll',
						'-webkit-background-size': 'cover',
						'-moz-background-size': 'cover',
						'-o-background-size': 'cover',
						'background-size': 'cover'
					});
				});
			}
		//Init

		//Video 
			$('body').on('click', '*[data-gallery="#video"]', function(){
				//Set ifraem values
					if( $(this).attr('data-source')=='vimeo' ){
						$('#Modal-Gallery .modal-body').html( '<iframe id="player" src="https://player.vimeo.com/video/'+$(this).attr('data-id')+'?api=1&player_id=player&autoplay=1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>' );
					}
					else if( $(this).attr('data-source')=='youtube' ){
						$('#Modal-Gallery .modal-body').html('<iframe id="player" src="https://www.youtube.com/embed/'+$(this).attr('data-id')+'?autoplay=1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>');
					}

				resizeVideo($(this).attr('data-source'), $(this).attr('data-id'));
				
				//Show modal
				$('#Modal-Gallery').modal('toggle');
			});


			$('#Modal-Gallery').on('hidden.bs.modal', function (e) {
				$('#Modal-Gallery .modal-body').html('');
			});
		//Video

		//Photo
			$('body').on('click', '*[data-gallery="#photo"]', function(){
				//Set values
				$('#Modal-Gallery .modal-body').html('<img src="'+$(this).attr('data-source')+'" alt=""/>');
				
				//Show modal
				$('#Modal-Gallery').modal('toggle');
			});
		//Photo
	//Modal Gallery
});


function resizeVideo(source, id){
	if( source == 'vimeo' ){
	  	$.post('http://sunrise.ru.com/_cdn/video/iframe-responsive/about-video.php', {TYPE: 'VIMEO', ID:id}, function(data){
			
			var eWidth = parseInt($('body').find('iframe#player').width() );
			var eHeight = eWidth / data.coef;

			console.log(eWidth + ' ' + eHeight);
		    //Resize video--------------------------------------
			$('body').find('iframe#player').css('height', eHeight+'px' );
		},'json');
	} // vimeo adaptation---------------------------------------
	else if( source == 'youtube' ){

		$.post('http://sunrise.ru.com/_cdn/video/iframe-responsive/about-video.php', {TYPE: 'YOUTUBE', ID:id}, function(data){
			
			var eWidth = parseInt($('body').find('iframe#player').width() );
			var eHeight = eWidth / data.coef;

			console.log(eWidth + ' ' + eHeight);
		    //Resize video--------------------------------------
			$('body').find('iframe#player').css('height', eHeight+'px' );
		},'json');

	} // youtube adaptation---------------------------------------
}// .resizeHeaderVideo

function iconInit(){
	$('body').find('i.icon').each(function(index){
		var src = $(this).attr('data-src');
		$(this).load(src);
	});
} // iconInit