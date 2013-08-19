$(function(){
    // control-mode. control for top and side mode (fixed or normal), you can remove it if you want..
    var control_mode = '<div class="control-mode" id="control-mode">'
    +'    <ul class="choice-mode grd-teal corner-bl hide">'
    +'        <li><a id="normal-mode" href="#normal-mode">Normal</a></li>'
    +'        <li><a id="fixedtop-mode" href="#fixedtop-mode">Fixed top</a></li>'
    +'        <li><a id="fixedside-mode" href="#fixedside-mode">Fixed Side</a></li>'
    +'        <li><a id="fixedsideonly-mode" href="#fixedsideonly-mode">Fixed Side Only</a></li>'
    +'    </ul>'
    +'    <div class="navigate-mode"><a href="#" class="grd-teal corner-bottom"><i class="typicn-cog"></i></a></div>'
    +'</div>';
    
    $('body').append(control_mode)
    if(sessionStorage.mode == undefined){
        sessionStorage.mode = 1;
    }
    
    $('#control-mode > .navigate-mode').click(function(e){
        $('#control-mode > .choice-mode').slideToggle(); // toggle slide hide
        
        return false;
    });
    $('html').on('click', function(){
        $('#control-mode > .choice-mode').slideUp(); // toggle slide hide
    });
    $('#normal-mode').click(function(){
        $('.header, .side-left, .side-right').removeClass('fixed');
        
        // set position by default
        $('.header').css({
            'top' : '0px'
        });
        $('.side-left, .side-right').css({
            'top' : '60px'
        });
        
        $('#control-mode > .choice-mode').slideToggle(); // toggle slide hide
        
        sessionStorage.mode = 1;
        return false;
    });
    $('#fixedtop-mode').click(function(){
        $('.header, .side-left, .side-right').removeClass('fixed'); // remove first to normalize class
        $('.header').addClass('fixed');
        
        // set position by default
        $('.header').css({
            'top' : '0px'
        });
        $('.side-left, .side-right').css({
            'top' : '60px'
        });
        
        $('#control-mode > .choice-mode').slideToggle(); // toggle slide hide
        
        sessionStorage.mode = 2;
        return false;
    });
    $('#fixedside-mode').click(function(){
        $('.header, .side-left, .side-right').removeClass('fixed'); // remove first to normalize class
        $('.header, .side-left, .side-right').addClass('fixed');
        
        // set position by default
        $('.header').css({
            'top' : '0px'
        });
        
        $('.side-left, .side-right').css({
            'top' : '60px'
        });
        
        $('#control-mode > .choice-mode').slideToggle(); // toggle slide hide
        
        sessionStorage.mode = 3;
        return false;
    });
    $('#fixedsideonly-mode').click(function(){
        $('.header, .side-left, .side-right').removeClass('fixed'); // remove first to normalize class
        $('.side-left, .side-right').addClass('fixed');
        
        // set position by default
        if($(window).scrollTop() > 60){
            $('.side-left, .side-right').css({
                'top' : '0px'
            });
        }
            
        $('#control-mode > .choice-mode').slideToggle(); // toggle slide hide
        
        sessionStorage.mode = 4;
        return false;
    });
    
    if(sessionStorage.mode){
        if(sessionStorage.mode == '1'){ // normal mode
            $('.header, .side-left, .side-right').removeClass('fixed');
        }
        if(sessionStorage.mode == '2'){ // fixed header only
            $('.header, .side-left, .side-right').removeClass('fixed'); // remove first to normalize class
            $('.header').addClass('fixed');
        }
        if(sessionStorage.mode == '3'){ // fixed all
            $('.header, .side-left, .side-right').removeClass('fixed'); // remove first to normalize class
            $('.header, .side-left, .side-right').addClass('fixed')
        }
        if(sessionStorage.mode == '4'){ // fixed side only
            $('.header, .side-left, .side-right').removeClass('fixed'); // remove first to normalize class
            $('.side-left, .side-right').addClass('fixed');
        }
        
        // help for responsive
        if(sessionStorage.mode == 4){
            // control for responsive
            if($(window).width() > 767){
                data_scroll = 60 - parseInt($(this).scrollTop());
                $('.side-left, .side-right').css({
                    'top' : data_scroll+'px'
                });
                $('body, html').animate({
                    scrollTop : 0
                })
            }
            else{
                $('.side-left, .side-right').css({
                    'top' : '0px'
                });
            }
        }
        else{
            if($(window).width() <= 767){
                $('.side-left, .side-right').css({
                    'top' : '0px'
                });
            }
            else{
                $('.side-left, .side-right').css({
                    'top' : '60px'
                });
            }
        }
    }
    
    // end control-mode
    
    // control for responsive
    $(window).resize(function(){
        if(sessionStorage.mode == 4){
            // control for responsive
            if($(window).width() > 767){
                data_scroll = 60 - parseInt($(this).scrollTop());
                $('.side-left, .side-right').css({
                    'top' : data_scroll+'px'
                });
                $('body, html').animate({
                    scrollTop : 0
                })
            }
            else{
                $('.side-left, .side-right').css({
                    'top' : '0px'
                });
            }
        }
        else{
            if($(window).width() <= 767){
                $('.side-left, .side-right').css({
                    'top' : '0px'
                });
            }
            else{
                $('.side-left, .side-right').css({
                    'top' : '60px'
                });
            }
        }
    });
    
    
    // scrolling event
    $(window).scroll(function() {
        
        // this for hide/show button to-top
        if($(this).scrollTop() > 480) {
            $('a[rel=to-top]').fadeIn('slow');	
        } else {
            $('a[rel=to-top]').fadeOut('slow');
        }
        
        // this for sincronize active sidebar item
        if($(this).scrollTop() > 35){
            $('.sidebar > li:first-child.active').removeClass('first');
        }
        else{
            $('.sidebar > li:first-child.active').addClass('first');
        }
        
        if(sessionStorage.mode){
            if(sessionStorage.mode == 4){
                if($(this).scrollTop() > 60){
                    $('.side-left, .side-right').css({
                        'top' : '0px'
                    });
                }
                else{
                    // control for responsive
                    if($(window).width() > 767){
                        data_scroll = 60 - parseInt($(this).scrollTop());
                        $('.side-left, .side-right').css({
                            'top' : data_scroll+'px'
                        });
                    }
                    else{
                        $('.side-left, .side-right').css({
                            'top' : '0px'
                        });
                    }
                }
            }
            else{
                $('.header').css({
                    'top' : '0px'
                });
            }
        }
        
    });
    
    $('a[rel=to-top]').click(function(e) {
        e.preventDefault();
        $('body,html').animate({
            scrollTop:0
        }, 'slow');
    });
    // end scroll to top
    
    
    // tooltip helper
    $('[rel=tooltip]').tooltip();	
    $('[rel=tooltip-bottom]').tooltip({
        placement : 'bottom'
    });	
    $('[rel=tooltip-right]').tooltip({
        placement : 'right'
    });	
    $('[rel=tooltip-left]').tooltip({
        placement : 'left'
    });	
    // end tooltip helper
    
    
    // animate scroll, define class scroll will be activate this
    $(".scroll").click(function(e){
        e.preventDefault();
        $("html,body").animate({scrollTop: $(this.hash).offset().top-60}, 'slow');
    });
    // end animate scroll
    
    
    // control box
    // collapse a box
    $('.header-control [data-box=collapse]').click(function(){
        var collapse = $(this),
        box = collapse.parent().parent().parent();

        collapse.find('i').toggleClass('icofont-caret-up icofont-caret-down'); // change icon
        box.find('.box-body').slideToggle(); // toggle body box
    });

    // close a box
    $('.header-control [data-box=close]').click(function(){
        var close = $(this),
        box = close.parent().parent().parent(),
        data_anim = close.attr('data-hide'),
        animate = (data_anim == undefined || data_anim == '') ? 'fadeOut' : data_anim;

        box.addClass('animated '+animate);
        setTimeout(function(){
            box.hide()
        },1000);
    });
    // end control box
    
    
})
