// navbar toggling
const navbarShowBtn = document.querySelector(".navbar-show-btn");
const navbarCollapseDiv = document.querySelector(".navbar-collapse");
const navbarHideBtn = document.querySelector(".navbar-hide-btn");

navbarShowBtn.addEventListener("click", function () {
  navbarCollapseDiv.classList.add("navbar-show");
});
navbarHideBtn.addEventListener("click", function () {
  navbarCollapseDiv.classList.remove("navbar-show");
});

// changing search icon image on window resize
window.addEventListener("resize", changeSearchIcon);
function changeSearchIcon() {
  let winSize = window.matchMedia("(min-width: 1200px)");
  if (winSize.matches) {
    document.querySelector(".search-icon img").src = "images/search-icon.png";
  } else {
    document.querySelector(".search-icon img").src =
      "images/search-icon-dark.png";
  }
}
changeSearchIcon();

// stopping all animation and transition
let resizeTimer;
window.addEventListener("rotation", () => {
  document.body.classList.add("resize-animation-stopper");
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => {
    document.body.classList.remove("resize-animation-stopper");
  }, 400);
});

document.addEventListener("DOMContentLoaded", function () {
  const navbarShowBtn = document.querySelector(".navbar-show-btn");
  const navbarHideBtn = document.querySelector(".navbar-hide-btn");
  const navbarCollapse = document.querySelector(".navbar-collapse");

  // Function to show navbar
  function showNavbar() {
    navbarCollapse.classList.add("navbar-show");
  }

  // Function to hide navbar
  function hideNavbar() {
    navbarCollapse.classList.remove("navbar-show");
  }

  // Toggle navbar when show button is clicked
  navbarShowBtn.addEventListener("click", showNavbar);

  // Toggle navbar when hide button is clicked
  navbarHideBtn.addEventListener("click", hideNavbar);
});
