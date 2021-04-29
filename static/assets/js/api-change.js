// const domain = 'http://127.0.0.1:8000'
document.querySelector('#change-form').addEventListener('submit', async (e) =>{
    e.preventDefault();
    let form = e.target;
    postdata = {
        old_password:form.old_password.value,
        new_password:form.new_password.value,
        new_password2:form.new_password.value,
    }

    
    // let csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').getAttribute('value');
    let response = await fetch(`http://${window.location.host}/az/api/auth/change/`, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${localStorage.getItem('Token')}`,
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