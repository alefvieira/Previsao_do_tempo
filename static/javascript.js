function Select_Page(){
    const valor = document.querySelector('input[name="regiao"]:checked').value

    regiao_capitais = document.querySelector("h2.regiao_capitais")
    
    chama_ret = ocu_visu_reg(valor)
    
    regiao_capitais.innerHTML = valor.toUpperCase()
    
}
Select_Page()

//QUANDO SE MANIPULA CLASSES E IDS É NECESSÁRIO CONCATENAR COM O SIMBOLO DO ATRIBUTO(ELEMENTO)

function ocu_visu_reg(valor){
    if (valor == "Sudeste"){
        document.querySelector(".Sul").style.display = "none"
        document.querySelector(".Norte").style.display = "none"
        document.querySelector(".Nordeste").style.display = "none"
        document.querySelector(".Centro-Oeste").style.display = "none"
        document.querySelector(".Sudeste").style.display = "block"
    }
    if (valor == "Sul"){
        document.querySelector(".Sul").style.display = "block"
        document.querySelector(".Norte").style.display = "none"
        document.querySelector(".Nordeste").style.display = "none"
        document.querySelector(".Centro-Oeste").style.display = "none"
        document.querySelector(".Sudeste").style.display = "none"
    }
    if (valor == "Centro-Oeste"){
        document.querySelector(".Sul").style.display = "none"
        document.querySelector(".Norte").style.display = "none"
        document.querySelector(".Nordeste").style.display = "none"
        document.querySelector(".Centro-Oeste").style.display = "block"
        document.querySelector(".Sudeste").style.display = "none"
    }
    if (valor == "Norte"){
        document.querySelector(".Sul").style.display = "none"
        document.querySelector(".Norte").style.display = "block"
        document.querySelector(".Nordeste").style.display = "none"
        document.querySelector(".Centro-Oeste").style.display = "none"
        document.querySelector(".Sudeste").style.display = "none"
    }
    if (valor == "Nordeste"){
        document.querySelector(".Sul").style.display = "none"
        document.querySelector(".Norte").style.display = "none"
        document.querySelector(".Nordeste").style.display = "block"
        document.querySelector(".Centro-Oeste").style.display = "none"
        document.querySelector(".Sudeste").style.display = "none"
    }
    return true

}

function atualizacao(){

    var p_atu=  document.getElementsByClassName("att").value
    
    
}

