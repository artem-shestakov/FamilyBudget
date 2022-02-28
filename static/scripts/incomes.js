document.addEventListener('click', function (e) {
    console.log(e.target);
  });

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
  
  if (track.offsetWidth - (index * carouselWidth) < carouselWidth) {
    next.classList.add('hide');
  }
})

prev.addEventListener('click', () => {
  index--;
  if (track.offsetWidth - (index * carouselWidth) <= carouselWidth) {
    next.classList.remove('hide');
    }
  
  if (index === 0) {
    prev.classList.remove('show');
  }
  track.style.transform = `translateX(-${index * carouselWidth}px)`;
})

$('#createIncome').click(function(){
    const csrftoken = getCookie('csrftoken');
    var incomeTitle = $('input[name="incomeTitle"]').val().trim();
    console.log(incomeTitle);
    data = {
        'title': incomeTitle
    };
    $.ajax({
        url: "{% url 'create_income' %}",
        method: "POST",
        headers: { 
            'X-CSRFToken': csrftoken
        },
        data: data,
        success: function(data) {
            console.log(data)
        }
    })
})
