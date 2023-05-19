isClicked = false;
products = []
listaAtual = {}

function openPopup(id) {
    document.querySelector(`.PopUp#${id}`).style.display = "block";
    document.getElementById("overlay").style.display = "block";
    if (id == "addProductToListPopUp") {
        document.getElementById("toAdd").innerHTML = `<h1>Adicionar esses produtos a lista ${listaAtual['listaNome']}</h1>`
        for (var i=0; i < products.length; i++) {
            document.getElementById("toAdd").innerHTML +=`
            <p>${products[i]['quantity']} ${products[i]['productName']}</p>
        `;
        }
    }
}

function closePopup() {
    var a = document.getElementsByClassName("PopUp");
    for (var i=0; i < a.length; i++) {
        a[i].style.display = "none";
    }
    document.getElementById("overlay").style.display = "none";
}

function showButton(idLp, idAp) {
    if (!isClicked) {
        document.querySelector(`.listItens#${idLp}`).style.display = "none";
        document.querySelector(`.addProductsToList#${idAp}`).style.display = "block";
    }
}

function hideButton(idLp, idAp) {
    if (!isClicked) {
        document.querySelector(`.listItens#${idLp}`).style.display = "block";
        document.querySelector(`.addProductsToList#${idAp}`).style.display = "none";
    }
}

function showProductsButton(idAp, listId, listName) {
    isClicked = !isClicked;
    var produtos = document.getElementsByClassName('plus');
    var quantity = document.getElementsByClassName('quantity');
    if (isClicked) {
        document.querySelector(`.addProductsToList#${idAp}`).value = "Cancelar";
        document.getElementById("floatAddProductsButton").style.display = "block";
        listaAtual = {'listId': listId, 'listaNome': listName}
        document.getElementById('listName').innerText = `Adicionar ${products.length} Produtos a Lista ${listName} `;
        for (var i=0; i < produtos.length; i++) {
            produtos[i].style.display = "block";
        }
    } else {
        document.querySelector(`.addProductsToList#${idAp}`).value = "Adicionar Produtos";
        document.getElementById("floatAddProductsButton").style.display = "none";
        products = []
        document.getElementById("toAdd").innerHTML = '';
        for (var i=0; i < produtos.length; i++) {
            produtos[i].style.display = "none";
            quantity[i].value = 1
        }
    }
}

function storeSelectedProducts(pId, pName) {
    products.push({'productId': pId, 'productName': pName, 'quantity': document.querySelector(`.quantity#id${pId}`).value});
    document.getElementById('listName').innerText = `Adicionar ${products.length} Produtos a Lista ${listaAtual['listaNome']} `;
}

function sendProducts() {
    id = listaAtual['listId'];
    console.log(id)
    const data = JSON.stringify({4: products})
    fetch('/add_multiple_products_to_list/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: data,
      })
}