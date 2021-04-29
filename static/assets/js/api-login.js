const domain = 'http://127.0.0.1:8000'
document.querySelector('#login-api').addEventListener('submit', async (e) =>{
    e.preventDefault();
    let form = e.target;
    postdata = {
        username:form.username.value,
        password:form.password.value,
    }
    // let csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').getAttribute('value');
    let response = await fetch(`http://${window.location.host}/az/api/auth/login/`, {
        headers: {
            'Content-Type': 'application/json',
            // 'X-CSRFToken': csrfToken
        },
        method: "POST",
        body: JSON.stringify(postdata)
    });
    data = await response.json();

    if (response.ok){
        localStorage.setItem('Token' , data.token)
        window.location.replace(domain)
    }

})