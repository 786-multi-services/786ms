$(window).bind('scroll', function () {
    if ($(window).scrollTop() > 20) {
        $('.navbar').addClass('navbar-inverse',300);
    } else {
        $('.navbar').removeClass('navbar-inverse',300);
    }
});

$(document).ready(function () {
		$(document).on("scroll", onScroll);
 
		$('a[href^="#"]').on('click', function (e) {
			e.preventDefault();
			$(document).off("scroll");
 
			$('a').each(function () {
				$(this).removeClass('active');
			})
			$(this).addClass('active');
 
			var target = this.hash;
			$target = $(target);
			$('html, body').stop().animate({
				'scrollTop': $target.offset().top+2
			}, 500, 'swing', function () {
				window.location.hash = target;
				$(document).on("scroll", onScroll);
			});
		});
	});
 
	function onScroll(event){
		var scrollPosition = $(document).scrollTop();
		$('a').each(function () {
			var currentLink = $(this);
			try{
				var refElement = $(currentLink.attr("href"));
				if (refElement.position().top <= scrollPosition && refElement.position().top + refElement.height() > scrollPosition) {
					$('nav ul li a').removeClass("active");
					currentLink.addClass("active");
				}
				else{
					currentLink.removeClass("active");
				}
			}
			catch(e){
			}
		});
	}
