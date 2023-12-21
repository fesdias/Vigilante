// scrolling-effect.js
function updateScrollPositions() {
    const scrollTop = window.scrollY;
    const parallaxElements = document.querySelectorAll('.parallax');
    
    parallaxElements.forEach(element => {
        const speed = parseFloat(element.getAttribute('data-speed')) || 1;
        const translateY = scrollTop * speed;
        element.style.transform = `translateY(${translateY}px)`;
    });
}

window.addEventListener('scroll', updateScrollPositions);
updateScrollPositions();