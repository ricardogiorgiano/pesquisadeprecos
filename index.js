const puppeteer = require('puppeteer');
const fs = require('fs')


//essa variavel é o produto que vai ser pesquisado
var produto = 'Iphone';

/*
        { 
        headless: false,
        defaultViewport: null}
 */


 (async () => {
     
    //headless para mostrar o chrome abrindo, e todo o processo        
    //defaultViewport para ajustar o tamanho da tela, para a tela inteira

    const browser = await puppeteer.launch()

    const page = await browser.newPage()
    //abre o market do google
    await page.goto("https://shopping.google.com/?nord=1") 
    //pesquisa o produto  
    await page.type("#REsRA", produto, {delay: 50})
    //aperta enter
    await page.keyboard.press('Enter');  
   await page.waitForNavigation();

  var dados = await page.evaluate(async () => {
    //Seleciona os dados
    const nodeImg = await document.querySelectorAll("div .ArOc1c > img")
    const nodePrice = await document.querySelectorAll('span .a8Pemb.OFFNJ')
    const nodeName = await document.querySelectorAll(".Xjkr3b")
    var arrayNode = [nodePrice, nodeName, nodeImg]

  
      //Percorre e cria um novo array só com os dados do json
    var arrayProdutos = []
    for (let x = 0; x < arrayNode[0].length; x++) {
        
        var preco = arrayNode[0][x].textContent
        var nome = arrayNode[1][x].textContent
        var img = arrayNode[2][x].src
        arrayProdutos.push({preco, nome, img})

    }
    return arrayProdutos
    
   })  

   //Salva os dados
   fs.writeFile("searchgoogle.json", JSON.stringify(dados, null, 2), err => {

    if(err) {
        throw new Error
    }


})
await browser.close()

})()