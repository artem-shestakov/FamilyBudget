;(function(){
    const toastEl = document.getElementById('toast')
    const toastBody = document.getElementById('toastBody')
    const toast = new bootstrap.Toast(toastEl)

    htmx.on('showMessage', (e) => {
        console.log('toast')
        toastBody.innerHTML = e.detail.value
        toast.show()
    })
})()