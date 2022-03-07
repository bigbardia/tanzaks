function LikeMeme(pk){
    let test =  $(`#${pk}`);
    let csrf = test.children()[0];
    csrf = csrf.value;


    $.ajax({
        url : "/",
        type : "post",
        data : {
            csrfmiddlewaretoken : csrf,
            pk : pk,
        },
        success: function(response){
            let btn = test.children()[2];
            btn.innerHTML = `LIKE : ${response[0]}`;
            
        }
        
    });
}
