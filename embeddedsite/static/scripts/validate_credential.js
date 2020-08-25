$(document).ready( ()=>{
        // send ajax request to see if username is taken
        $('#signup-form #id_username').blur(function(){
            let username = $('#signup-form #id_username').val();
            if(username.length !== ''){
                $.ajax({
                    url: '/username/',
                    dataType: 'Json',
                    data: {'username': username},
                    success: function(data){
                        if(data.result === true){
                            $('#signup-form #id_username').css({'background-color':'red', 'color':'white'});
                        }
                        else{
                            $('#signup-form #id_username').css({'background-color':'green', 'color':'white'});
                        }
                    },
                    error: function(data){
                        alert('error')
                    }
                });
            }
        });
        // send ajax request to see if email is taken.
        $('#signup-form #id_email').blur(function(){
            let email = $('#signup-form #id_email').val();
            if(email.length !== ''){
                $.ajax({
                    url: '/email/',
                    dataType: 'Json',
                    data: {'email': email},
                    success: function(data){
                        if(data.result === true){
                            $('#signup-form #id_email').css({'background-color':'red', 'color':'white'});
                        }
                        else{
                            $('#signup-form #id_email').css({'background-color':'green', 'color':'white'});
                        }
                    },
                    error: function(data){
                        alert('error');
                    }
                });
            }
        });

});