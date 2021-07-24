document.addEventListener("DOMContentLoaded",() => {

    const pincel = {
        ativo: false,
        movendo: false,
        pos: { x:0 , y:0 },
        posA: null
    }

    const tela = document.querySelector('#tela')
    const context = tela.getContext('2d')

    tela.width = 700
    tela.height = 500

    context.lineWidth = 3

    const drawLine = (linha) => {

    context.beginPath()
    context.moveTo(linha.posA.x,linha.posA.y)
    context.lineTo(linha.pos.x,linha.pos.y)
    context.stroke()
    }

    tela.onmousedown = () => {pincel.ativo = true}
    tela.onmouseup = () => {pincel.ativo = false}

    tela.onmousemove = (evento) => {
        pincel.pos.x = evento.clientX
        pincel.pos.y = evento.clientY
        pincel.movendo = true
    }

    const ciclo = () => {
        if (pincel.ativo && pincel.movendo && pincel.posA) {
            drawLine({ pos: pincel.pos, posA: pincel.posA })
            pincel.movendo = false
        }
        pincel.posA = { x: pincel.pos.x , y: pincel.pos.y}

        setTimeout(ciclo, 10)

        let cor = document.querySelector('input#cor').value
        let tamanho = document.querySelector('input#tamanho').value
        context.strokeStyle = cor
        context.lineWidth = tamanho
    }
    ciclo()

})