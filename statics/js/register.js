$(function(){
    function getCookie(name){
        var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
        return x ? x[1]:undefined;
    }
   //检查两次密码是否一致
    $('#register').on('click',function(){
        username = $('#username').val();
        email = $('#email').val();
        password = $('#password').val();
        confirm_password = $('#confirm_password').val();
        if(username='' || email==''|| password==''|| confirm_password==''){
            alert('参数不能为空！');
            return false;
        }
        if(password!=confirm_password){
            alert('两次密码不一致！')
            return false;
        }

        var arr_data = $('#register_form').serialize();

        $.ajax({
            url:'/register',
            method:'post',
            data:arr_data,
            cache:false,
            success:function(data){
                if(data==1){
                    window.location.href="/";
                }else{
                    alert(data)
                }
            },
            error:function(e){
                console.log(e);
            }
        });

    });


});