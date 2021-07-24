function gerar() {
    let num = document.getElementById('txtn')
    let tab = document.getElementById('seltab')
    if (num.value.length == 0) {
        alert('por favor, digite um número')
    } else {
        let n = Number(num.value)
        tab.innerHTML = ''
        for (i=1; i<=10; i++) {
            let item = document.createElement('option')
            item.text = `${n} x ${i} = ${n*i}`
            item.value = `tab${i}`
            tab.appendChild(item)
        }
    }
}