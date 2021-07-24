function verify() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')
    if (fano.value.length != 4 || fano.value > ano) {
        alert('dados inválidos ou não preenchidos, verifique novamente.')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var gen = ''
        if (fsex[0].checked) {
            gen = 'Homem'
        } else if (fsex[1].checked) {
            gen = 'Mulher'
        }
        res.style.textAlign = 'center'
        res.innerHTML = `${gen} com ${idade} anos`
    }
}