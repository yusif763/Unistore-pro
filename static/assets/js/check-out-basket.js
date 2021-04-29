async function  myfunction(product_id){
  let element = document.querySelector(`[data-id1="${product_id}"]`)
  let inputValue = document.getElementById(`count${product_id}`).value
  inputValue = parseInt(inputValue) + 1
  let qiymetDeyish = parseInt(document.getElementById(`price${product_id}`).innerText)
  if (document.getElementById('qiymet2') !== null){
    qiymet = parseInt(document.getElementById('qiymet2').innerText)
    qiymet += qiymetDeyish
    document.getElementById('qiymet2').innerText = `${qiymet}`
    if (document.getElementById(`endirim${product_id}`) === null){
      qiymet2 = parseInt(document.getElementById('qiymet').innerText)
      qiymet2 += qiymetDeyish
      document.getElementById('qiymet').innerText = `${qiymet2}`
    }
  }
  if(document.getElementById(`endirim${product_id}`) !== null){
    let qiymetDeyish2 = parseInt(document.getElementById(`endirim${product_id}`).innerText)
    if (document.getElementById('qiymet2') !== null){
      qiymet2 = parseInt(document.getElementById('qiymet').innerText)
      qiymet2 += qiymetDeyish2
      document.getElementById('qiymet').innerText = `${qiymet2}`
    }
  }
  if(document.getElementById(`check${product_id}`) !== null){
    document.getElementById(`check${product_id}`).value = inputValue;
  }
  let plusCount = {
          product: product_id,
          count: inputValue
        };
        let response = await fetch(`http://${window.location.host}/az/check-api/orders/`,{
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${localStorage.getItem("Token")}`,
            // 'X-CSRFToken': csrfToken
          },
          method: "POST",
          body: JSON.stringify(plusCount),
        })
      }


async function  myfunction2(product_id){
  let element = document.querySelector(`[data-id2="${product_id}"]`)
  let inputValue2 = document.getElementById(`count${product_id}`).value
  let qiymetDeyish = parseInt(document.getElementById(`price${product_id}`).innerText)
  if (document.getElementById('qiymet2') !== null){
    if(inputValue2 > 1){
      qiymet = parseInt(document.getElementById('qiymet2').innerText)
      qiymet -= qiymetDeyish
      document.getElementById('qiymet2').innerText = `${qiymet}`
      if (document.getElementById(`endirim${product_id}`) === null){
        qiymet2 = parseInt(document.getElementById('qiymet').innerText)
        qiymet2 -= qiymetDeyish
        document.getElementById('qiymet').innerText = `${qiymet2}`
      }
    }else{
      return
    }
  }
  if(document.getElementById(`endirim${product_id}`) !== null){
    let qiymetDeyish2 = parseInt(document.getElementById(`endirim${product_id}`).innerText)
    if (document.getElementById('qiymet2') !== null){
      if(inputValue2 > 1){
        qiymet2 = parseInt(document.getElementById('qiymet').innerText)
        qiymet2 -= qiymetDeyish2
        document.getElementById('qiymet').innerText = `${qiymet2}`
    }else{
      return
    }
  }
}
  inputValue2 = parseInt(inputValue2) - 1
  if(document.getElementById(`check${product_id}`) !== null){
    document.getElementById(`check${product_id}`).value = inputValue2;
  }
  let minusCount = { 
          product: product_id,
          count: inputValue2
        };
        console.log(minusCount)
        let response = await fetch(`http://${window.location.host}/az/check-api/orders/`,{
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${localStorage.getItem("Token")}`,
            // 'X-CSRFToken': csrfToken
          },
          method: "POST",
          body: JSON.stringify(minusCount),
        })
        console.log(response.json())
      }




async function  myfunction3(product_id){
  let element = document.querySelector(`[data-id3="${product_id}"]`)
  let inputValue3 = document.getElementById(`check${product_id}`).value
  inputValue3 = parseInt(inputValue3) + 1
  let qiymetDeyish = parseInt(document.getElementById(`price${product_id}`).innerText)
  if (document.getElementById('qiymet') !== null){
    qiymet = parseInt(document.getElementById('qiymet2').innerText)
    qiymet += qiymetDeyish
    document.getElementById('qiymet2').innerText = `${qiymet}`
    if (document.getElementById(`endirim${product_id}`) === null){
      qiymet2 = parseInt(document.getElementById('qiymet').innerText)
      qiymet2 += qiymetDeyish
      document.getElementById('qiymet').innerText = `${qiymet2}`
    }
  }
  if(document.getElementById(`endirim${product_id}`) !== null){
    let qiymetDeyish2 = parseInt(document.getElementById(`endirim${product_id}`).innerText)
    if (document.getElementById('qiymet2') !== null){
      qiymet2 = parseInt(document.getElementById('qiymet').innerText)
      qiymet2 += qiymetDeyish2
      document.getElementById('qiymet').innerText = `${qiymet2}`
    }
  }
  if(document.getElementById(`check${product_id}`) !== null){
    document.getElementById(`count${product_id}`).value = inputValue3;
  }
  let plusCount3 = {
          product: product_id,
          count: inputValue3
        };
        let response = await fetch(`http://${window.location.host}/az/check-api/orders/`,{
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${localStorage.getItem("Token")}`,
            // 'X-CSRFToken': csrfToken
          },
          method: "POST",
          body: JSON.stringify(plusCount3),
        })
        console.log(response.json())
      }
      



async function  myfunction4(product_id){
  let element = document.querySelector(`[data-id4="${product_id}"]`)
  let inputValue4 = document.getElementById(`count${product_id}`).value
  let qiymetDeyish = parseInt(document.getElementById(`price${product_id}`).innerText)
  if (document.getElementById('qiymet2') !== null){
    if(inputValue4 > 1){
      qiymet = parseInt(document.getElementById('qiymet2').innerText)
      qiymet -= qiymetDeyish
      document.getElementById('qiymet2').innerText = `${qiymet}`
      if (document.getElementById(`endirim${product_id}`) === null){
        qiymet2 = parseInt(document.getElementById('qiymet').innerText)
        qiymet2 -= qiymetDeyish
        document.getElementById('qiymet').innerText = `${qiymet2}`
      }
    }else{
      return
    }
  }
  if(document.getElementById(`endirim${product_id}`) !== null){
    let qiymetDeyish2 = parseInt(document.getElementById(`endirim${product_id}`).innerText)
    if (document.getElementById('qiymet2') !== null){
      if(inputValue4 > 1){
        qiymet2 = parseInt(document.getElementById('qiymet').innerText)
        qiymet2 -= qiymetDeyish2
        document.getElementById('qiymet').innerText = `${qiymet2}`
    }else{
      return
    }
  }
}
  inputValue4 = parseInt(inputValue4) - 1
  if(document.getElementById(`check${product_id}`) !== null){
    document.getElementById(`count${product_id}`).value = inputValue4;
  }
  let minusCount4 = {
          product: product_id,
          count: inputValue4
        };
        console.log(minusCount4)
        let response = await fetch(`http://${window.location.host}/az/check-api/orders/`,{
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${localStorage.getItem("Token")}`,
            // 'X-CSRFToken': csrfToken
          },
          method: "POST",
          body: JSON.stringify(minusCount4),
        })
        console.log(response.json())
      }