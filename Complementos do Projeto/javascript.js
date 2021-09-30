
function block_pag(){
    var filtro_block = document.querySelector(".filtro_block")
    filtro_block.style.display = "inline-block"
    var block_body = document.querySelector("body")
    block_body.style.overflow = "hidden"
    var cadastre = document.querySelector(".cadastre")
    cadastre.style.display = "inline-block"

}

function fechar_cadastro(){
    var block_body = document.querySelector("body")
    block_body.style.overflow = "visible"

    var filtro_block = document.querySelector(".filtro_block")
    filtro_block.style.display = "none"
}