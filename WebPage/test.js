const scrollContainer = document.getElementById('scroll-container');
const scrollLeft = document.getElementById('scroll-left');
const scrollRight = document.getElementById('scroll-right');
const sectionWidth = scrollContainer.offsetWidth;

scrollLeft.addEventListener('click', () => {
    scrollContainer.scrollBy({
        left: -sectionWidth,
        behavior: 'smooth'
    });
});

scrollRight.addEventListener('click', () => {
    scrollContainer.scrollBy({
        left: sectionWidth,
        behavior: 'smooth'
    });
});
