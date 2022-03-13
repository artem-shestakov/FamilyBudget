prev  = document.querySelector('.prev');
next = document.querySelector('.next');
track = document.querySelector('.track');
carouselWidth = document.querySelector('.carousel-container').clientWidth;
index = 0;

(function() {
  prev.classList.add('hide')
  if (track.scrollWidth - (index * carouselWidth) <= carouselWidth) {
      next.classList.add('hide');
  }
})()

window.addEventListener('resize', () => {
  carouselWidth = document.querySelector('.carousel-container').clientWidth;
})

next.addEventListener('click', () => {
  index++;
  prev.classList.remove('hide');
  prev.classList.add('show');
  track.style.transform = `translateX(-${index * carouselWidth}px)`;
  if (track.scrollWidth - (index * carouselWidth) <= carouselWidth) {
    next.classList.add('hide');
  }
})

prev.addEventListener('click', () => {
  if (index > 0) {
    index--;
  }
  
  if (track.scrollWidth - (index * carouselWidth) <= carouselWidth) {
    next.classList.remove('hide');
  }
  
  if (index === 0) {
    prev.classList.remove('show');
    prev.classList.add('hide');
  }
  track.style.transform = `translateX(-${index * carouselWidth}px)`;
})
