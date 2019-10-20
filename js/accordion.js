$(document).ready(function() {

  $(".panel").css("display", "none")

  $(".accordion").click(function(e) {
    var $panel = $(this).next()
    $(".panel").slideUp()
    var accordionid = e.target.id

    if ($panel.css("display") == "none") {
      $panel.slideDown()
      $("#" + accordionid).attr('symbol-plus', "-")
    } else {
      $panel.slideUp()
      $("#" + accordionid).attr('symbol-plus', "+")
    }
  })
})
