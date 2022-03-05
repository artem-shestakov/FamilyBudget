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
      e.detail.shouldSwap = false
    } 
  })

  htmx.on('hidden.bs.modal', (e) => {
    document.getElementById('incomeAddDialog').innerHTML = ''
  })
})()
