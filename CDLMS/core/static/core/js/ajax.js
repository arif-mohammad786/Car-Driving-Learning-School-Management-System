$("#adminlogin").click(function(){
    let username=$("#username").val();    
    let password=$("#password").val();  
    let csr=$("input[name='csrfmiddlewaretoken']").val();
    // console.log(username);  
    // console.log(password);  
    if(username == ""){
        $("#msg").html("<h4 class='text-warning'>Please Enter Username</h4>");
    }
    if(password == ""){
        $("#msg").html("<h4 class='text-warning'>Please Enter Password</h4>");
    }else{
        mydata={username:username,password:password,csrfmiddlewaretoken:csr};
        $.ajax({
            url:"/adminuser/adminlogin/",
            method:"POST",
            data:mydata,
            success:function(data){
                if(data.status == 1){
                    window.location.href="/adminuser/dashboard/";
                }     
                if(data.status == 0){
                    window.location.href="/";
                }           
            }
        })
    }
})

