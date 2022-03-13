let prev;
let next;
let track;
let carouselWidth;
let index;

function sourceDragging() {
    const sources = document.querySelectorAll('.image.source')

    sources.forEach(source => {
        source.addEventListener('dragstart', () => {
            source.classList.add('dragging')
        })
        source.addEventListener('dragend', () => {
            source.classList.remove('dragging')
        })
    })
}

function savingDroping() {
    const savings = document.querySelectorAll('.image.saving')
    
    savings.forEach(saving => {
        saving.addEventListener('dragstart', () => {
            saving.classList.add('dragging')
        })
        saving.addEventListener('dragend', () => {
            saving.classList.remove('dragging')
        })
    })
}

(function() {
    htmx.on('htmx:afterRequest', (e) => {
        if (e.detail.target.id === 'sources') {
            sourceDragging()
        } else if (e.detail.target.id === 'savings') {
            savingDroping()
        }
      })    
})()

