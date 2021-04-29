

// window.addEventListener("load", async function () {
//     let response = await fetch(domain+window.URLS['productDetail'], {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//     });
//     console.log("dadadadadadadad")

//        let responseData = await response.json()
//        console.log(responseData['comment_count'])
//         if (response.ok){
//             let commenCountElement = document.getElementById('comment-count')
//             commenCountElement.innerText = responseData['comment_count'];
//             let commentListElement = document.getElementById('comment-list')
//             console.log(responseData)
//             for (i of responseData['comment']){
//                 commentListElement.innerHTML += `<li class="comment">
//                 <div class="vcard bio">
//                     <img src="${i['author']['image']}" alt="Image placeholder">
//                 </div>
//                 <div class="comment-body">
//                     <h3 id="comment-author">${i['author']['first_name']}</h3>
//                     <div class="meta" >October 03, 2018 at 2:21pm</div>
//                     <p id="comment-content">${i['content']}</p>
//                     <p><a href="#" class="reply">Reply</a></p>
//                 </div>
//             </li>`
//             }
//         }else{
//             alert('Something went wrong');
//         }
// });


// console.log("bunedi")
// window.addEventListener("load", async function () {
//     let response = await fetch(`http://${window.location.host}/az/api/product/`, {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//     });

//        let responseData = await response.json()
//        if (response.ok){
//          let productListElement = document.getElementById('product-list')

//          // let url = window.URLS['productDetail']
//          for (i of responseData){
//           //  console.log(window.URLS['productItem'].replace('3', `'${i[id]}'`))
//           //     let url = window.URLS['productItem'].replace('3', `'${i[id]}'`)
//                 // url.replace('1234567',`${i['id']}`);
//                 if (i['faiz'] === null){
//                     productListElement.innerHTML += `
//                     <div class="col-sm-6 col-md-4 product">
//                     <div class="body">
//                     <a href="#"  class="favorites addfav"  data-favorite="inactive"><i class="ion-ios-heart-outline"></i></a>
//                       <a href="${domain}/product/product/${i['id']}"><img src="${i['main_image']}" alt="Apple iMac 27 Retina"/></a>
//                       <div class="content">
//                         <h1 class="h3">${i['short_title']}</h1>
//                         <p class="price">${i['price']}</p>
//                         <label>${i['category']}</label>
//                         <button class="btn btn-link"> <i class="ion-android-open"></i> Details</button>
//                         <button data-id = "${i['id']}" data-action="add" class="addcard" class="btn btn-primary btn-sm rounded"> <i class="ion-bag"></i> Add to cart</button>
//                       </div>
//                     </div>
//                   </div>`

//                 }
//                 else{
//                     productListElement.innerHTML += `
//                     <div class="col-sm-6 col-md-4 product">
//                     <div class="body">
//                     <a href="#" data-addcart = "${i['id']}" class="favorites addfav" data-action="add" data-favorite="inactive"><i class="ion-ios-heart-outline"></i></a>
//                       <a href="${domain}/product/product/${i['id']}"><img src="${i['main_image']}" alt="Apple iMac 27 Retina"/></a>
//                       <div class="content">
//                         <h1 class="h3">${i['short_title']}</h1>
//                         <p class="price">${i['endirim']}</p>
//                         <p class="price through">${i['price']}</p>
//                         <label>${i['category']}</label>
//                         <button class="btn btn-link"> <i class="ion-android-open"></i> Details</button>
//                         <button data-id = "${i['id']}" data-action="add" class="addcard" class=" btn btn-primary btn-sm rounded"> <i class="ion-bag"></i> Add to cart</button>
//                       </div>
//                     </div>
//                   </div>`

//                 }
//             }
//         }else{
//             alert('Something went wrong');
//         }
// });








