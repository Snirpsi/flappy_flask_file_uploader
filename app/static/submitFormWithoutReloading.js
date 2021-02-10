$(document).ready(function (){
    $("form").submit(function(event){
        event.preventDefault()
        var abstand = document.getElementById('abstand').value
        var winkel = document.getElementById('winkel').value
        var csrf_token = document.getElementById("csrf_token").value
        
        //ajax post request
        $.post('#',{csrf_token:csrf_token,abstand:abstand,winkel:winkel},function(data){
            console.log(data)
            document.getElementById("csrf-token")

        })
    })
})