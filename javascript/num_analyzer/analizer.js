let itens = []
let txtn = document.querySelector('input#txtn')
let tab = document.querySelector('select#seltab')
let res = document.querySelector('div#res')

function isValid(n) {
    if (Number(n) >= 1 && Number(n) <= 100) {
        return true
    } else {
        return false
    }
}

function inItens(n,i) {
    if (i.indexOf(Number(n)) != -1) {
        return true
    } else {
        return false
    }
}

function adicionar(){
    if (!isValid(txtn.value) || inItens(txtn.value, itens)){
        alert('Elemento ja registrado')
    } else {
        res.innerHTML = ''
        //if (txtn.value.length == 0 || txtn.value >= 10 || txtn.value <= 0){
        //    alert('Elemento Inválido ou não especificado')
        //} else {
            itens.push(Number(txtn.value))
            let item = document.createElement('option')
            item.text = `Valor ${txtn.value} adicionado`
            tab.appendChild(item)
        }
    txtn.value = ''
    txtn.focus()
    }
    

function finalizar(){
    if (itens.length == 0) {
        alert('insira um valor')
    } else {
        let tot = itens.length
        let mai = itens[0]
        let men = itens[0]
        let som = 0
        for (let pos in itens) {
            if (itens[pos] > mai) {
                mai = itens[pos]
            }
            if (itens[pos] < men) {
                men = itens[pos]
            }
        }
        for(let pos in itens){
            som += itens[pos]
        }
        let med = som/tot
        res.innerHTML = ''
        res.innerHTML += `<p>ao todo, temos ${tot} números</p>`
        res.innerHTML += `<p>o maior valor é ${mai}</p>`
        res.innerHTML += `<p>o menor valor é ${men}</p>`
        res.innerHTML += `<p>a soma de todos os valores é ${som}</p>`
        res.innerHTML += `<p>a média de todos os valores é ${med}</p>`
    }
}