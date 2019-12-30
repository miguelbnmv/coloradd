var form = document.getElementById("hiddenForm");
var menu = document.getElementById("hiddenMenu");


function revealForm() {
  form.style.display = "block";
  if(form.style.display == "block"){
    menu.style.display = "none";
  }
}

var span = document.getElementsByClassName("close")[0];
span.onclick = function() {
  form.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == form) {
    form.style.display = "none";
  }
}
