$(document).ready(function(){
    $("#owl-demo").owlCarousel({

    navigation : true,
    slideSpeed : 300,
    paginationSpeed : 400,
    navigationText : [" "," "],
    singleItem : true,
    scrollPerPage : false,
    pagination: true


    // "singleItem:true" is a shortcut for:
    // items : 1, 
    // itemsDesktop : false,
    // itemsDesktopSmall : false,
    // itemsTablet: false,
    // itemsMobile : false

    });

    $(".fancybox").fancybox({
        helpers : {
            title: {
                type: 'inside',
                /*position: 'top'*/
            }
        },
        beforeLoad: function() {
            this.title = $(this.element).next('.desc').html();

        }
    });


    // $('.slidertab .img img').hoverpulse({
    //     size: 170,  // number of pixels to pulse element (in each direction)
    //     speed: 400 // speed of the animation 
    // });

});

