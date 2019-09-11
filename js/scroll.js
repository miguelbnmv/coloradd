$(document).ready(function() {
  $(window).on('scroll', function(){
    if($(window).scrollTop()) {
      $('nav').addClass('hidden');
    }
    else {
      $('nav').removeClass('hidden');
    }
  })
})
