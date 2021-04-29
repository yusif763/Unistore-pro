

let qiymet = 0
let qiymet2 = 0
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
  if (response.ok){
    let checkElement = document.getElementById('check-out-basket')
      console.log(responseData)
     // let url = window.URLS['productDetail']
     for (i of responseData){
       if (i['product']['faiz'] == null){
        checkElement.innerHTML += `<div class="media" id="remove${i['id']}">
        <div class="media-left">
          <a href="#">
            <img class="media-object" src="${i['product']['main_image']}" alt="iPad Air"/>
          </a>
        </div>
        <div class="media-body">
          <h2 class="h4 media-heading">${i['product']['short_title']}</h2>
          <label>${i['product']['category']}</label>
          <br>
          <p style="display: inline !important;" id="price${i["product"]["id"]}" class="price">${i['product']['price']}</p><span style="display: inline !important;">$</span>
        </div>
        <div class="controls">
          <div class="input-group">
            <span class="input-group-btn">
              <button data-id4="${i["product"]["id"]}" id="checkminus${i["product"]["id"]}" onclick="myfunction4(${i["product"]["id"]})" class="btn btn-default btn-sm" type="button" data-action="minus"><i class="ion-minus-round"></i></button>
            </span>
            <input id="check${i["product"]["id"]}" type="text" class="form-control input-sm" placeholder="Qty" value="${i['count']}" readonly="">
            <span class="input-group-btn">
              <button data-id3="${i["product"]["id"]}" id="checkplus${i["product"]["id"]}" onclick="myfunction3(${i["product"]["id"]})" class="btn btn-default btn-sm" type="button" data-action="plus"><i class="ion-plus-round"></i></button>
            </span>
          </div><!-- /input-group -->

          <a  onclick="deletefunction1(${i["id"]})" href="#remove"> <i class="ion-trash-b"></i> Remove </a>
        </div>
      </div>`

      qiymet += parseInt(i["product"]["price"]) * parseInt(i['count'])
      qiymet2 += parseInt(i["product"]["price"]) * parseInt(i['count'])
       }
       else{

        checkElement.innerHTML += `<div class="media" id="remove${i['id']}">
        <div class="media-left">
          <a href="#">
            <img class="media-object" src="${i['product']['main_image']}" alt="iPad Air"/>
          </a>
        </div>
        <div class="media-body">
          <h2 class="h4 media-heading">${i['product']['short_title']}</h2>
          <label>${i['product']['category']}</label>
          <br>
          <p style="display: inline !important;" id="endirim${i["product"]["id"]}" class="price">${i['product']['endirim']}</p><span style="display: inline !important;">$</span>
          <p id="price${i["product"]["id"]}" style="display: none;" >${i['product']['price']}</p>
        </div>
        <div class="controls">
          <div class="input-group">
            <span class="input-group-btn">
              <button data-id4="${i["product"]["id"]}" id="checkminus${i["product"]["id"]}" onclick="myfunction4(${i["product"]["id"]})" class="btn btn-default btn-sm" type="button" data-action="minus"><i class="ion-minus-round"></i></button>
            </span>
            <input id="check${i["product"]["id"]}" type="text" class="form-control input-sm" placeholder="Qty" value="${i['count']}" readonly="">
            <span class="input-group-btn">
              <button data-id3="${i["product"]["id"]}" id="checkplus${i["product"]["id"]}" onclick="myfunction3(${i["product"]["id"]})" class="btn btn-default btn-sm" type="button" data-action="plus"><i class="ion-plus-round"></i></button>
            </span>
          </div><!-- /input-group -->

          <a onclick="deletefunction1(${i["id"]})" href="#remove"> <i class="ion-trash-b"></i> Remove </a>
        </div>
      </div>`
      qiymet += parseInt(i["product"]["endirim"]) * parseInt(i['count'])
      qiymet2 += parseInt(i["product"]["price"]) * parseInt(i['count'])
       
       }
        }
    }
  else {
    alert("Something went wrong");
  }

  document.getElementById('qiymet2').innerText = `${qiymet2}`
  document.getElementById('qiymet').innerText = `${qiymet}`

});