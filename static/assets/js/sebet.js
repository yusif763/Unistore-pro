// console.log('sebet')
// window.addEventListener("load", async function () {
//     let response = await fetch(`http://${window.location.host}/en/check-api/orders/`, {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/json',
//             'Authorization': `Token ${localStorage.getItem('Token')}`,
//         },
//     });

//        let responseData = await response.json()
//        if (response.ok){
//         document.getElementById('mCSB_1').style.display = "none";
//          let sebetElement = document.getElementById('sebetichi')
//           console.log(responseData)
//          // let url = window.URLS['productDetail']
//          for (i of responseData){


//            console.log(i['product'])
//            if (i['product']['faiz'] == null){
//             sebetElement.innerHTML += `
//                     <div class="media">
//           <div class="media-left">
//             <a href="#">
//               <img class="media-object" src="${i['product']['main_image']}" alt="HP Chromebook 11"/>
//             </a>
//           </div>
//           <div class="media-body">
//             <h2 class="h4 media-heading">${i['product']['short_title']}</h2>
//             <label>${i['product']['category']}</label>
//             <p class="price">${i['product']['price']}$</p>
//           </div>
//           <div class="controls">
//             <div class="input-group">
//               <span class="input-group-btn">
//                 <button class="btn btn-default btn-sm" type="button" data-action="minus"><i class="ion-minus-round"></i></button>
//               </span>
//               <input type="text" class="form-control input-sm" placeholder="Qty" value="${i['count']}" readonly="">
//               <span class="input-group-btn">
//                 <button class="btn btn-default btn-sm" type="button" data-action="plus"><i class="ion-plus-round"></i></button>
//               </span>
//             </div>`
//            }
//            else{

//                sebetElement.innerHTML += `
//                <div class="media">
//      <div class="media-left">
//        <a href="#">
//          <img class="media-object" src="${i['product']['main_image']}" alt="HP Chromebook 11"/>
//        </a>
//      </div>
//      <div class="media-body">
//        <h2 class="h4 media-heading">${i['product']['short_title']}</h2>
//        <label>${i['product']['category']}</label>
//        <p class="price">${i['product']['endirim']}$</p>
//      </div>
//      <div class="controls">
//        <div class="input-group">
//          <span class="input-group-btn">
//            <button class="btn btn-default btn-sm" type="button" data-action="minus"><i class="ion-minus-round"></i></button>
//          </span>
//          <input type="text" class="form-control input-sm" placeholder="Qty" value="${i['count']}" readonly="">
//          <span class="input-group-btn">
//            <button class="btn btn-default btn-sm" type="button" data-action="plus"><i class="ion-plus-round"></i></button>
//          </span>
//        </div>`
//            }
//             }
//         }else{
//             alert('Something went wrong');
//         }
// });



