function contar() {
  const ini = document.getElementById("txti").value;
  const fim = document.getElementById("txtf").value;
  const passo = document.getElementById("txtp").value;
  const res = document.getElementById("res");
  if (ini.length == 0 || fim.length == 0 || passo.length == 0) {
    res.innerHTML = "Impossível Contar";
  } else {
    res.innerHTML = "Contagem: <br>";
    let i = Number(ini);
    let f = Number(fim);
    let p = Number(passo);
    if (p <= 0) {
      window.alert("Passo Inválido! Considerando Passo = 1");
      p = 1;
    }
    if (i < f) {
      // progressiva
      for (let c = i; c <= f; c += p) {
        res.innerHTML += `${c} \u{1F449}`;
      }
    } else {
      // regressiva
      for (let c = i; c >= f; c -= p) {
        res.innerHTML += `${c} \u{1F449}`;
      }
    }
    res.innerHTML += `\u{1F3C1}`;
  }
}
