function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

;(function(){
  var incomeModal = new bootstrap.Modal(document.getElementById('incomeModal'))

  htmx.on('htmx:afterSwap', (e) => {
    if (e.detail.target.id === 'incomeAddDialog') {
      incomeModal.show()
    } 
  })

  htmx.on('htmx:beforeSwap', (e) => {
    if (e.detail.target.id === 'incomeAddDialog' && !e.detail.xhr.response) {
      incomeModal.hide()
    } 
  })
})()

const prev  = document.querySelector('.prev');
const next = document.querySelector('.next');

const track = document.querySelector('.track');

let carouselWidth = document.querySelector('.carousel-container').offsetWidth;

window.onload = function() {
    if (track.offsetWidth - (index * carouselWidth) <= carouselWidth) {
        next.classList.add('hide');
    }
};

window.addEventListener('resize', () => {
  carouselWidth = document.querySelector('.carousel-container').offsetWidth;
})

let index = 0;

next.addEventListener('click', () => {
  index++;
  prev.classList.add('show');
  track.style.transform = `translateX(-${index * carouselWidth}px)`;
  console.log(index, track.offsetWidth, carouselWidth)
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
