var canvas, ctx, ALTURA, LARGURA, frames = 0,

chao = {
    y: 550,
    altura: 50,
    cor: "greenyellow",
    desenha: function() {
        ctx.fillStyle = this.cor
        ctx.fillRect(0, this.y, LARGURA, this.altura)
    }
},

player = {
    x:50,
    y:0,
    largura:50,
    altura:50,
    cor: "grey",
    gravidade: 0.5,
    velocidade: 0,
    forca: this.gravidade,
    atualiza: function() {
        this.velocidade += this.gravidade
        this.y += this.velocidade

        if (this.y > chao.y - this.altura) {
            this.y = chao.y - this.altura
        }
    },
    pula: function() {
        this.velocidade = -this.forca
    },
    desenha: function() {
        ctx.fillStyle = this.cor
        ctx.fillRect(this.x, this.y, this.largura, this.altura)
    }
}

function clique(event) {
    player.pula()
}

function main() {
    ALTURA = window.innerHeight
    LARGURA = window.innerWidth

    if (LARGURA >= 500) {
        LARGURA = 600
        ALTURA = 600
    }

    canvas = document.createElement("canvas")
    canvas.width = LARGURA
    canvas.height = ALTURA
    canvas.style.border = '1px solid #000'

    ctx = canvas.getContext("2d")
    document.body.appendChild(canvas)
    document.addEventListener('mousedown', clique)

    roda()
}

function roda() {
    atualiza()
    desenha()

    window.requestAnimationFrame(roda)
}

function atualiza() {
    frames++
    player.atualiza()
}

function desenha() {
    ctx.fillStyle = "skyblue"
    ctx.fillRect(0, 0, LARGURA, ALTURA)
    chao.desenha()
    player.desenha()
}


main()