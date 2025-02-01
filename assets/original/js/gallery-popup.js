$(function(){
   $('#portfolio').magnificPopup({
      delegate: 'a',
      type: 'image',
      tClose: 'Close (Esc)', // Alt text on close button
  		tLoading: 'Loading...', // Text that is displayed during loading. Can contain %curr% and %total% keys
		gallery: {
         enabled:'true',
			tPrev: 'Previous (Left arrow key)', // Alt text on left arrow
			tNext: 'Next (Right arrow key)', // Alt text on right arrow
			tCounter: '%curr% of %total%' // Markup for<strong></strong> "1 of 7" counter
      },
      image: {
         tError: 'A imagem não pode ser carregada.'
      },
      mainClass: 'mfp-zoom-in',
      removalDelay: 300, //delay removal by X to allow out-animation
      callbacks: {
         beforeOpen: function() {
            $('#portfolio a').each(function(){
               $(this).attr('title', $(this).find('img').attr('alt'));
            }); 
         },
         open: function() {
            //overwrite default prev + next function. Add timeout for css3 crossfade animation
            $.magnificPopup.instance.next = function() {
               var self = this;
               self.wrap.removeClass('mfp-image-loaded');
               setTimeout(function() { $.magnificPopup.proto.next.call(self); }, 120);
            },
            $.magnificPopup.instance.prev = function() {
               var self = this;
               self.wrap.removeClass('mfp-image-loaded');
               setTimeout(function() { $.magnificPopup.proto.prev.call(self); }, 120);
            }
         },
         imageLoadComplete: function() { 
            var self = this;
            setTimeout(function() { self.wrap.addClass('mfp-image-loaded'); }, 16);
         }
      }
   });
});