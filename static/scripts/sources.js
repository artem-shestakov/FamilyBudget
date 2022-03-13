;(function(){
  var sourceModal = new bootstrap.Modal(document.getElementById('sourceModal'))

  htmx.on('htmx:afterSwap', (e) => {
    if (e.detail.target.id === 'sourceAddDialog') {
      sourceModal.show()
    } 
  })

  htmx.on('htmx:beforeSwap', (e) => {
    if (e.detail.target.id === 'sourceAddDialog' && !e.detail.xhr.response) {
      sourceModal.hide()
      e.detail.shouldSwap = false
    } 
  })

  htmx.on('hidden.bs.modal', (e) => {
    document.getElementById('sourceAddDialog').innerHTML = ''
  })
})()
