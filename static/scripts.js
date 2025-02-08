

const metodos = document.querySelectorAll("input[name='metodo_de_pagamento']")
const dados = document.querySelector("#dados-do-cartao")

metodos.forEach(metodo => {
    metodo.addEventListener("change", (e) => {
        if (metodo.value === "1" || metodo.value === "2") {
            console.log("isso")
            dados.classList.remove("hide")
        } else {
            console.log("não é isso")
            dados.classList.add("hide")
        }})})


