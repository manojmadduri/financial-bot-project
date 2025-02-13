// script.js
document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('nav-links');
  const topBar = document.querySelector('.top-bar');
  const middleBar = document.querySelector('.middle-bar');
  const bottomBar = document.querySelector('.bottom-bar');

  hamburger.addEventListener('click', () => {
    // Toggle nav link visibility
    navLinks.classList.toggle('show');

    // Animate hamburger bars
    topBar.classList.toggle('open');
    middleBar.classList.toggle('open');
    bottomBar.classList.toggle('open');
  });
});
