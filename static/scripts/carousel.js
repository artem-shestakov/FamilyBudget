prev  = document.querySelector('.prev');
next = document.querySelector('.next');
track = document.querySelector('.track');
carouselWidth = document.querySelector('.carousel-container').offsetWidth;
index = 0;

window.onload = function() {
    if (track.offsetWidth - (index * carouselWidth) <= carouselWidth) {
        next.classList.add('hide');
    }
};

window.addEventListener('resize', () => {
  carouselWidth = document.querySelector('.carousel-container').offsetWidth;
})

next.addEventListener('click', () => {
  index++;
  prev.classList.add('show');
  track.style.transform = `translateX(-${index * carouselWidth}px)`;
  if (track.offsetWidth - (index * carouselWidth) <= carouselWidth) {
    next.classList.add('hide');
  }
})

prev.addEventListener('click', () => {
  if (index > 0) {
    index--;
  }
  if (track.offsetWidth - (index * carouselWidth) <= carouselWidth) {
    next.classList.remove('hide');
    }
  
  if (index === 0) {
    prev.classList.remove('show');
  }
  track.style.transform = `translateX(-${index * carouselWidth}px)`;
})
