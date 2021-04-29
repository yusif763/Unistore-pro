// var domain = 'http://127.0.0.1:8000';
document.querySelector('#register_form').addEventListener('submit', async (e) =>{
    e.preventDefault();
    let form = e.target;
    postdata = {
        email:form.email.value,
        first_name:form.first_name.value,
        last_name:form.last_name.value,
        username:form.username.value,
        bio:form.bio.value,
        password:form.password.value,
        password2:form.password2.value
    }
    console.log('dasadda');
    // let csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').getAttribute('value');
    console.log(window.location.host)
    // console.log(postData.entries());
    let response = await fetch(`http://${window.location.host}/az/api/auth/register/`, {
        headers: {
            'Content-Type': 'application/json',
            // 'X-CSRFToken': csrfToken
        },
        
        method: "POST",
        body:JSON.stringify(postdata)
    });
    console.log('dfmnsdfnmsds')
    console.log(response);
    data = await response.json();
})