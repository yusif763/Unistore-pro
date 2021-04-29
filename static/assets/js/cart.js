window.addEventListener("load", async function () {
  let response = await fetch(
    `http://${window.location.host}/en/check-api/orders/`,
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("Token")}`,
      },
    }
  );

  let responseData = await response.json();
  if (response.ok) {
    document.getElementById("mCSB_1").style.display = "none";
    let sebetElement = document.getElementById("sebetichi");
    document.getElementById("sebet-count").innerText = "";
    document.getElementById("sebet-count").innerText = responseData.length;
    for (i of responseData) {
      if (i["product"]["faiz"] == null) {
        sebetElement.innerHTML += `
                    <div class="media" id="for-remove${i['id']}" data-id="${i["product"]["id"]}">
          <div class="media-left">
            <a href="#">
              <img class="media-object" src="${i["product"]["main_image"]}" alt="HP Chromebook 11"/>
            </a>
          </div>
          <div class="media-body">
            <h2 class="h4 media-heading">${i["product"]["short_title"]}</h2>
            <label>${i["product"]["category"]}</label>
            <br>
            <p style="display: inline !important;" id="price${i["product"]["id"]}" class="price">${i['product']['price']}</p><span style="display: inline !important;">$</span>
          </div>
          <div class="controls">
            <div class="input-group" id="budu">
              <span class="input-group-btn" id="bunnan-sora">
                <button data-id2="${i["product"]["id"]}" id="minus${i["product"]["id"]}" onclick="myfunction2(${i["product"]["id"]})" class="btn btn-default btn-sm" type="button" data-action="minus"><i class="ion-minus-round"></i></button>
              </span>
              <input id="count${i["product"]["id"]}" type="text" class="form-control input-sm" placeholder="Qty" value="${i["count"]}" readonly="">
              <span class="input-group-btn" id="bunnan-evvel">
                <button data-id1="${i["product"]["id"]}" id="plus${i["product"]["id"]}" onclick="myfunction(${i["product"]["id"]})" class="ustegel btn btn-default btn-sm" type="button" data-action="plus"><i class="ion-plus-round"></i></button>
              </span>
            </div>
            <a onclick="deletefunction2(${i["id"]})" href="#remove"> <i class="ion-trash-b"></i> Remove </a>
            </div>`;
            
      } else {
        sebetElement.innerHTML += `
               <div class="media" id="for-remove${i['id']}" data-id="${i["product"]["id"]}">
     <div class="media-left">
       <a href="#">
         <img class="media-object" src="${i["product"]["main_image"]}" alt="HP Chromebook 11"/>
       </a>
     </div>
     <div class="media-body">
       <h2 class="h4 media-heading">${i["product"]["short_title"]}</h2>
       <label>${i["product"]["category"]}</label>
       <br>
       <p style="display: inline !important;" id="endirim${i["product"]["id"]}" class="price">${i['product']['endirim']}</p><span style="display: inline !important;">$</span>
      <p id="price${i["product"]["id"]}" style="display: none;" >${i['product']['price']}</p>
     </div>
     <div class="controls">
       <div class="input-group">
         <span class="input-group-btn" id="bunnan-sora">
           <button data-id2="${i["product"]["id"]}" id="minus${i["product"]["id"]}" onclick="myfunction2(${i["product"]["id"]})" class="btn btn-default btn-sm" type="button" data-action="minus"><i class="ion-minus-round"></i></button>
         </span>
         <input type="text" id="count${i["product"]["id"]}" class="form-control input-sm" placeholder="Qty" value="${i["count"]}" readonly="">
         <span class="input-group-btn">
           <button data-id1="${i["product"]["id"]}" id="plus${i["product"]["id"]}" onclick="myfunction(${i["product"]["id"]})" class="ustegel btn btn-default btn-sm" type="button" data-action="plus"><i class="ion-plus-round"></i></button>
         </span>
       </div>
       <a onclick="deletefunction2(${i["id"]})" href="#remove"> <i class="ion-trash-b"></i> Remove </a>
        </div>`;
        
      }
    }

  }
  
  else {
    alert("Something went wrong");
  }
});

let addCart = document.getElementsByClassName("addcard");
for (var i = 0; i < addCart.length; i++) {
  addCart[i].addEventListener("click", async (e) => {
    let card = e.target;
    var productId = card.dataset.addcart;
    let element = document.querySelector(`[data-id1="${productId}"]`)
    if ((inputValue = document.getElementById(`count${productId}`)) === null){
      inputValue = 1
    }
    else{
      inputValue = parseInt(inputValue.value) + 1
    }
    let postProduct = {
      product: productId,
      count: inputValue,
    };



    // let csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').getAttribute('value');
    let response = await fetch(`http://${window.location.host}/az/check-api/orders/`,{
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${localStorage.getItem("Token")}`,
        },
        method: "POST",
        body: JSON.stringify(postProduct),
      }
    );

    let sebetiArtir = document.getElementsByClassName("media");
    for (var i = 0; i < sebetiArtir.length; i++) {
      let varmi = sebetiArtir[i].getAttribute("data-id");
      if (productId === varmi){
        let tapArtir = document.getElementById(`count${productId}`).value;
        tapArtir = parseInt(tapArtir) + 1;
        document.getElementById(`count${productId}`).value = tapArtir;
        return;
      }
    }

    data = await response.json();
    let reqem = document.getElementById("sebet-count").innerText;
    reqem = parseInt(reqem);
    reqem += 1;
    document.getElementById("sebet-count").innerText = reqem;
    // let content = data.content;
    let ulElement = document.getElementById("sebetichi");
    let response2 = await fetch(
      `http://${window.location.host}/en/api/product/${data["product"]}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${localStorage.getItem("Token")}`,
        },
      }
    );
    data2 = await response2.json();
    if (data2["faiz"] == null) {
      ulElement.innerHTML += `
      <div class="media" data-id="${data2["id"]}">
<div class="media-left">
<a href="#">
<img class="media-object" src="${data2["main_image"]}" alt="HP Chromebook 11"/>
</a>
</div>
<div class="media-body">
<h2 class="h4 media-heading">${data2["short_title"]}</h2>
<label>${data2["category"]}</label>
<br>
<p style="display: inline !important;" id="price${data2["id"]}" class="price">${data2['price']}</p><span style="display: inline !important;">$</span>
</div>
<div class="controls">
<div class="input-group" id="budu">
<span class="input-group-btn" id="bunnan-sora">
  <button data-id2="${data2["id"]}" id="minus${data2["id"]}" onclick="myfunction2(${data2["id"]})" class="btn btn-default btn-sm" type="button" data-action="minus"><i class="ion-minus-round"></i></button>
</span>
<input id="count${data2["id"]}" type="text" class="form-control input-sm" placeholder="Qty" value="${data["count"]}" readonly="">
<span class="input-group-btn" id="bunnan-evvel">
  <button data-id1="${data2["id"]}" id="plus${data2["id"]}" onclick="myfunction(${data2["id"]})" class="ustegel btn btn-default btn-sm" type="button" data-action="plus"><i class="ion-plus-round"></i></button>
</span>
</div>
<a href="#remove"> <i class="ion-trash-b"></i> Remove </a>
</div>`;
    } else {
      ulElement.innerHTML += `
      <div class="media" data-id="${data2["id"]}">
<div class="media-left">
<a href="#">
<img class="media-object" src="${data2["main_image"]}" alt="HP Chromebook 11"/>
</a>
</div>
<div class="media-body">
<h2 class="h4 media-heading">${data2["short_title"]}</h2>
<label>${data2["category"]}</label>
<br>
<p style="display: inline !important;" id="endirim${data2["id"]}" class="price">${data2['endirim']}</p><span style="display: inline !important;">$</span>
<p id="price${data2["id"]}" style="display: none;" >${data2['price']}</p>
</div>
<div class="controls">
<div class="input-group">
<span class="input-group-btn" id="bunnan-sora">
  <button data-id2="${data2["id"]}" id="minus${data2["id"]}" onclick="myfunction2(${data2["id"]})" class="btn btn-default btn-sm" type="button" data-action="minus"><i class="ion-minus-round"></i></button>
</span>
<input type="text" id="count${data2["id"]}" class="form-control input-sm" placeholder="Qty" value="${data["count"]}" readonly="">
<span class="input-group-btn">
  <button data-id1="${data2["id"]}" id="plus${data2["id"]}" onclick="myfunction(${data2["id"]})" class="ustegel btn btn-default btn-sm" type="button" data-action="plus"><i class="ion-plus-round"></i></button>
</span>
</div>
<a href="#remove"> <i class="ion-trash-b"></i> Remove </a>
</div>`;
    }
  });
}




