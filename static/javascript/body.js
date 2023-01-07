
//varloader
var loader = document.getElementById("preloader");
window.addEventListener("load", function () {
  loader.style.display = "none";
});


window.addEventListener("load", function () {
  this.setTimeout(function open(event) {
    document.querySelector(".popup").style.display = "block;";
  }, 1000);
});

document.querySelector("#close").addEventListener("click", function () {
  document.querySelector(".popup").style.display = "none";
});

//
$.letItSnow("main", {
  stickyFlakes: "lis-flake--js",
  makeFlakes: true,
  sticky: true,
});
