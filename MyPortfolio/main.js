
let nav = document.querySelector(".header");
window.onscroll = function () {
  if (document.documentElement.scrollTop > 50) {
    nav.classList.add("header-scrolled");
  } else {
    nav.classList.remove("header-scrolled");
  }
};
var myCarousel = new bootstrap.Carousel(document.getElementById('carouselExampleIndicators'), {
  interval: 1000 
});


