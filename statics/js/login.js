function getCookie(name){
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1]:undefined;
}
$("#login").click(function(){
    var user = $("#username").val();
    var pwd = $("#password").val();
    var pd = {"username":user,"password":pwd,"_xsrf":getCookie("_xsrf")};
    $.ajax({
        type:"post",
        url:"/",
        data:pd,
        catch:false,
        success:function(data){
            window.location.href="/user";
        },
        error:function(){
            alert('error');
        }
    })
})