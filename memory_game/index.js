const cards = document.querySelectorAll(".card")
console.log(cards);

var isFlipped = false;
var first;
var second;

cards.forEach((card) => card.addEventListener("click", flip))

function flip() {

  this.classList.add("flip");
  if (!isFlipped) {
     isFlipped = true;
     first = this;
  } else {
    second = this;
    console.log(first);
    console.log(second);
    checkIt();
  }
}
 
function checkIt() {
if (first.dataset.image === second.dataset.image){
  success()
}else(
  fail()
)
};

var success = () => {
 
   first.removeEventListener('click',File);
  second.removeEventListener('click',File);
   reset()

}
 var fail =() => {
setTimeout( () => {
  first.classList.remove("flip");
  second.classList.remove("flip");
   reset()
}, 500)
}
var reset = () => {
   isFlipped = false;
   first = null;
   second = null;
   console.log("super!!")

}
(function shuffle() {
  cards.forEach((card) => {
    var index = Math.floor(Math.random()* 16);
      card.style.order = index;
  });
})();