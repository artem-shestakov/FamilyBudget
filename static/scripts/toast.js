function deleteHidenToast() {
    var toastElList = [].slice.call(document.querySelectorAll('#toast'))
    for (let toast in toastElList) {
        if (toastElList[toast].classList.contains('hide')) {
            toastElList[toast].outerHTML = "";
        }
    }
}

function showToasts() {
    var toastElList = [].slice.call(document.querySelectorAll('#toast'))
    var toastList = toastElList.map(function(toastEl) {
        return new bootstrap.Toast(toastEl)
    });
    toastList.forEach(toast => toast.show());
}

;(function(){
    const toastList = document.getElementById('toast-container')
    const toastEl = document.getElementById('toast-tmp')
    const toastBody = document.getElementById('toastBody')
    const toast = new bootstrap.Toast(toastEl)

    htmx.on('showMessage', (e) => {
        deleteHidenToast()
        toastBody.innerHTML = e.detail.value
        let clone = toastEl.cloneNode( true );
        clone.setAttribute( 'id', 'toast' );
        toastList.appendChild(clone)
        showToasts()
    })
})()