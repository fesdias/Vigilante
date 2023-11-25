document.addEventListener('scroll', function() {
  const scrolled = window.scrollY;
  const scale = 1 + (scrolled / 5000); // Adjust the divisor to control the speed of the scaling effect
  document.querySelector('.parallax-bg').style.transform = `scale(${scale})`;
});