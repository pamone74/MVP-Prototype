document.addEventListener("DOMContentLoaded", function () {
  const root = document.documentElement;

  // Array of colors
  const colors = ["#FFFFF5", "#FFFFF8", "#FFFFF6", "#FFFFF3", "#FFFFF4"];

  // Function to change color theme
  function changeColorTheme() {
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    root.style.setProperty("--primary-color", randomColor);
  }

  // Change color theme every minute
  setInterval(changeColorTheme, 60000); // 60000 milliseconds = 1 minute
});
