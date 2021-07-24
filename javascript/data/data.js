function carregar() {    
    const msg = document.getElementById('msg')
    const img = document.getElementById('imagem')
    const data = new Date()
    let hora = data.getHours()
    let min = data.getMinutes()
    msg.innerHTML = `Agora são <strong>${hora}h ${min}m</strong>`
    if (hora < 12) {
        img.src = 'manha.png'
        document.body.style.background = 'linear-gradient(skyblue, wheat)'
    } else if (hora < 18) {
        img.src = 'tarde.png'
        document.body.style.background = 'linear-gradient(#0e6edd, #FEAAA3, #543D6B)'
    } else {
        img.src = 'noite.png'
        document.body.style.background = 'linear-gradient(#011328, #2A3B4B)'
    }
    setTimeout(carregar, 1000)
}
