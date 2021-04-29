async function  deletefunction2(order_id){
    let response = await fetch(`http://${window.location.host}/az/check-api/orders/${order_id}`,{
    headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("Token")}`,
        // 'X-CSRFToken': csrfToken
    },
    method: "DELETE",
    })
    if( document.getElementById(`remove${order_id}`) !== null){
        removedElemenet = document.getElementById(`remove${order_id}`)
        removedElemenet.remove()
    }
    var sebetCountChanger = parseInt(document.getElementById('sebet-count').innerText)
    sebetCountChanger -= 1 
    document.getElementById('sebet-count').innerText = sebetCountChanger
}
async function  deletefunction1(order_id){
    let response = await fetch(`http://${window.location.host}/az/check-api/orders/${order_id}`,{
    headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("Token")}`,
        // 'X-CSRFToken': csrfToken
    },
    method: "DELETE",
    })
    if( document.getElementById(`for-remove${order_id}`) !== null){
        removedElemenet = document.getElementById(`for-remove${order_id}`)
        removedElemenet.remove()
    }
    var sebetCountChanger = parseInt(document.getElementById('sebet-count').innerText)
    sebetCountChanger -= 1 
    document.getElementById('sebet-count').innerText = sebetCountChanger
}


