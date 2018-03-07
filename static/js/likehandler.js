$(document).ready(function(){
  $(".like").click(function(){
       var recipeId = $(this).attr('id').slice(0, -1);
     $.ajax({url: "/recipies/like/"+recipeId,
            success: function() {
              $("#"+recipeId+'l').load(location.href+" #"+recipeId+"l>*","");
            },
          error: function() {
            alert("something broke");
          }});

   });

   $(".save").click(function(){
        var recipeId = $(this).attr('id').slice(0, -1);
      $.ajax({url: "/recipies/save/"+recipeId,
             success: function() {
               $("#"+recipeId+'s').load(location.href+" #"+recipeId+"s>*","");
             },
           error: function() {
             alert("something broke");
           }});

    })

    $(".editButton").click(function() {

    });


});
