
$(document).ready(function(){
    // handle search for a product
    $('#products-search-form').submit( function(){
        let searchKey = $('#search-input').val();
        if(searchKey === ''){
            return false;
        }
        else{
            alert(searchKey);
            $.ajax(
                {
                    url:  '/searchproducts/',
                    dataType: 'Json',
                    data: {'searchKey': searchKey},
                    success: function(data){
                        if(data.result.length === 0){
                            alert('no result');
                        }
                        else{
                            alert(data.result.length);
                           $.each(data.result, function(index){
                               alert(data.result[index].name);
                           });
                        }
                    },
                    error: function(data){
                        alert(' Error');
                    }
                }
            )
        }
        return false;
    });

    // handle search for tutorials
    $('#tutorials-search-form').submit( function(){
        alert('tutorial search');
        let searchKey = $('#search-input').val();
        if(searchKey === ''){
            return false;
        }
        else{
            alert(searchKey);
            $.ajax(
                {
                    url:  '/searchtutorials/',
                    dataType: 'Json',
                    data: {'searchKey': searchKey},
                    success: function(data){
                        if(data.result.length === 0){
                            alert('no result');
                        }
                        else{
                            alert(data.result.length);
                           $.each(data.result, function(index){
                               alert(data.result[index].name);
                           });
                        }
                    },
                    error: function(data){
                        alert(' Error');
                    }
                }
            )
        }
        return false;
    });

    // handle search for projects
    $('#projects-search-form').submit( function(){
        alert('projects search');
        let searchKey = $('#search-input').val();
        if(searchKey === ''){
            return false;
        }
        else{
            alert(searchKey);
            $.ajax(
                {
                    url:  '/searchprojects/',
                    dataType: 'Json',
                    data: {'searchKey': searchKey},
                    success: function(data){
                        if(data.result.length === 0){
                            alert('no result');
                        }
                        else{
                            alert(data.result.length);
                            $.each(data.result, function(index){
                                alert(data.result[index].name);
                            });
                        }
                    },
                    error: function(data){
                        alert(' Error');
                    }
                }
            )
        }
        return false;
    });

        
      // handle search for services
    $('#services-search-form').submit( function(){
        alert('services search');
        let searchKey = $('#search-input').val();
        if(searchKey === ''){
            return false;
        }
        else{
            alert(searchKey);
            $.ajax(
                {
                    url:  '/searchservices/',
                    dataType: 'Json',
                    data: {'searchKey': searchKey},
                    success: function(data){
                        if(data.result.length === 0){
                            alert('no result');
                        }
                        else{
                            alert(data.result.length);
                        $.each(data.result, function(index){
                            alert(data.result[index].name);
                        });
                        }
                    },
                    error: function(data){
                        alert(' Error');
                    }
                }
            )
        }
        return false;
    });


      // handle search for circuit
      $('#circuits-search-form').submit( function(){
        alert('circuits search');
        let searchKey = $('#search-input').val();
        if(searchKey === ''){
            return false;
        }
        else{
            alert(searchKey);
            $.ajax(
                {
                    url:  '/searchcircuits/',
                    dataType: 'Json',
                    data: {'searchKey': searchKey},
                    success: function(data){
                        if(data.result.length === 0){
                            alert('no result');
                        }
                        else{
                            alert(data.result.length);
                           $.each(data.result, function(index){
                               alert(data.result[index].name);
                           });
                        }
                    },
                    error: function(data){
                        alert(' Error');
                    }
                }
            )
        }
        return false;
    });

    // change input background and font colors on focus and out of focus
    $(':text, search, email, textarea').focus(function(){
        $(this).css({'background-color': 'black', 'color':'white'});
    });
    $(':text, search, email, textarea').blur(function(){
        $(this).css({'background-color': 'white', 'color':'black'});
    });

    // handle focus and change events for password input field
    $(':password').on(
        {
        change:(function(){
            if($(this).val().length > 0 && $(this).val().length < 8){
                $(this).css({'background-color': 'red'});
            }
            else{
                $(this).css({'background-color': 'green', 'color':'black'});
            }
        }),

        focus: function(){
            if( $(this).val().length > 0 && $(this).val().length < 8){
                $(this).css({'background-color': 'red'});
            }

            else if($(this).val().length >= 8){
                $(this).css({'background-color': 'green', 'color':'black'});
            }

            else{
                $(this).css({'background-color': 'black', 'color':'white'});
            }
        },
        blur: function(){
        
            if($(this).val().length >= 8){
                $(this).css({'background-color': 'green', 'color':'black'});
            }
         
            else{
                $(this).css({'background-color': 'red', 'color':'black'});
            }
        }
            
    });
    // when search button is hovered and left
    $('button.round-btn').hover(
        function(){
            $(this).attr({'class':'btn btn-danger rounded-circle'}).css({'border-radius':'0px 3px 3px 0px'});
            $('li.fa-search').attr({'class':'fa fa-search text-light'}).css('font-size', 'large');
        },
        function(){
            $(this).attr({'class':'btn btn-light'}).css({'border-radius':'0px 3px 3px 0px'});
            $('li.fa-search').attr({'class':'fa fa-search text-danger'});
        },
    );

    // when items such as tutorials, products are focus
    $('.multiple-items').hover(function(){
        $(this).css({'border':'1px solid rgb(0, 150, 0)'});
    },
    function(){
        $(this).css({'border':'0px solid rgb(255, 255, 255)'});
    }
    );

      // when anchored list items are hovered and left
      $('li a > span').hover(function(){
        $(this).attr({'class':'text-dark bg-light'});
    },
    function(){
        $(this).attr({'class':'text-dark bg-warning'});
    }
    );

});

