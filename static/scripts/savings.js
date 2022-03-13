;(function(){
  var savingModal = new bootstrap.Modal(document.getElementById('savingModal'))

  htmx.on('htmx:afterSwap', (e) => {
    if (e.detail.target.id === 'savingAddDialog') {
      savingModal.show()
    } 
  })

  htmx.on('htmx:beforeSwap', (e) => {
    if (e.detail.target.id === 'savingAddDialog' && !e.detail.xhr.response) {
      savingModal.hide()
      e.detail.shouldSwap = false
    } 
  })

  htmx.on('hidden.bs.modal', (e) => {
    document.getElementById('savingAddDialog').innerHTML = ''
  })
})()
