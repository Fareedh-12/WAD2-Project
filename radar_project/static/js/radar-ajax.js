$(document).ready(function() { 
$(this).css('color','red')
    $(".like_post_btn").click(function(){
        var getPostId;
        getPostId = $(this).attr('post-id');
        $.get('/radar/like_post/', {'post_id': getPostId},
        function(data){
            var name = data.post_id
            var selector = document.getElementsByName(name);
            
            $(selector).html("Likes : " + data.total_likes);

            // update button color depending on whether they have been liked
            console.log(data.liked)
            if(data.liked){
                $("i."+name).css("color","red");
            }else{
                $("i."+name).css("color","grey");
            }
        }
        );
    });



    $("#login_form").on("submit", function(){
        // adding some ajax functionality of login form
    })

    $("#sign-up-form").on("submit", function(){
        // adding some ajax functionality of signup form
    })

});
