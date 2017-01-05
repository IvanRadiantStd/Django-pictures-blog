$(function() {

	//SVG Fallback
	if(!Modernizr.svg) {
		$("img[src*='svg']").attr("src", function() {
			return $(this).attr("src").replace(".svg", ".png");
		});
	};

	//E-mail Ajax Send
	$("form").submit(function() { //Change
		var th = $(this);
		$.ajax({
			type: "POST",
			url: "mail.php", //Change
			data: th.serialize()
		}).done(function() {
			alert("Thank you!");
			setTimeout(function() {
				// Done Functions
				th.trigger("reset");
			}, 1000);
		});
		return false;
	});

	//Chrome Smooth Scroll
	try {
		$.browserSelector();
		if($("html").hasClass("chrome")) {
			$.smoothScroll();
		}
	} catch(err) {

	};

	/*********Filter tabs************/

	$("img, a").on("dragstart", function(event) { event.preventDefault(); });
	
	$(".filter-tab-item").not(":first").hide();
	$(".filter-wrapper .filter-tab").click(function() {

		$(".filter-wrapper .filter-tab").removeClass("active").eq($(this).index()).addClass("active");
		$(".filter-tab-item").hide().eq($(this).index()).fadeIn()

		$(".sidebar-slider").slick('reinit'); 
	}).eq(0).addClass("active");

	/************end****************/

	/******tag-cloud********/
	$.fn.tagcloud.defaults = {
	  size: {start: 10, end: 18, unit: 'pt'},
	  color: {start: '#eee', end: '#fff'}
	};

	$('.tagCloud a').tagcloud();
	/*********end**************/

	/*******equal heights*******/

	//$('.equal-heights-columns').equalHeights();

	$( document ).ready(function() {
    	$('.equal-heights-columns').equalHeights();
	});
	$(window).resize(function(){
		$('.equal-heights-columns').equalHeights();
	});


	/*******end***************/

	/******Slick-slider********/

	$('.sidebar-slider').slick({
		fade: true
	});


	/*********end**************/
	
	/*********Magnific Popup*****************/

	$('.popup-with-zoom-anim').magnificPopup({
		type: 'inline',

		fixedContentPos: false,
		fixedBgPos: true,

		overflowY: 'auto',

		closeBtnInside: true,
		preloader: false,
		
		midClick: true,
		removalDelay: 300,
		mainClass: 'my-mfp-zoom-in'
	});




	/***************************************/
	
	/**********EZDZ quick*****************/
		$('[type="file"]').ezdz({
		  
		  text: 'Перетащите картинку или кликните',
		  
		  validators: {
		    maxWidth: 2600,
		    maxHeight: 2600
		  },
		  
		  reject: function(file, errors) {
		    
		    if (errors.mimeType) {
		      alert(file.name + 'Файл должен быть изображением');
		    }
		      
		    if (errors.maxWidth) {
		      alert(file.name + ' изображение должно быть не выше 2600px');
		    }

		    if (errors.maxHeight) {
		      alert(file.name + ' изображение должно быь не ниже 2600px');
		    }
		    
		  }
		});

	/****************END******************/


});

