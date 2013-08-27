function dyn_notice() {
    var percent = 0;
    var notice = $.pnotify({
        title: "Please Wait",
        type: 'info',
        icon: 'picon picon-throbber',
        hide: false,
        closer: false,
        sticker: false,
        opacity: .75,
        shadow: false,
        width: "150px"
    });

    setTimeout(function() {
        notice.pnotify({
            title: false
        });
        var interval = setInterval(function() {
            percent += 2;
            var options = {
                text: percent + "% complete."
            };
            if (percent == 80) options.title = "Almost There";
            if (percent >= 100) {
                window.clearInterval(interval);
                options.title = "Done!";
                options.type = "success";
                options.hide = true;
                options.closer = true;
                options.sticker = true;
                options.icon = 'picon picon-task-complete';
                options.opacity = 1;
                options.shadow = true;
                options.width = $.pnotify.defaults.width;
            //options.min_height = "300px";
            }
            notice.pnotify(options);
        }, 120);
    }, 2000);
}
/*********** Positioned Stack ***********
* This stack is initially positioned through code instead of CSS.
* This is done through two extra variables. firstpos1 and firstpos2
* are pixel values, relative to a viewport edge. dir1 and dir2,
* respectively, determine which edge. It is calculated as follows:
*
* - dir = "up" - firstpos is relative to the bottom of viewport.
* - dir = "down" - firstpos is relative to the top of viewport.
* - dir = "right" - firstpos is relative to the left of viewport.
* - dir = "left" - firstpos is relative to the right of viewport.
*/
var stack_topleft = {
    "dir1": "down", 
    "dir2": "right", 
    "push": "top"
};
var stack_bottomleft = {
    "dir1": "right", 
    "dir2": "up", 
    "push": "top"
};
var stack_custom = {
    "dir1": "right", 
    "dir2": "down"
};
var stack_custom2 = {
    "dir1": "left", 
    "dir2": "up", 
    "push": "top"
};
var stack_bar_top = {
    "dir1": "down", 
    "dir2": "right", 
    "push": "top", 
    "spacing1": 0, 
    "spacing2": 0
};
var stack_bar_bottom = {
    "dir1": "up", 
    "dir2": "right", 
    "spacing1": 0, 
    "spacing2": 0
};
var stack_bottomright = {
    "dir1": "up", 
    "dir2": "left", 
    "firstpos1": 25, 
    "firstpos2": 25
};

function show_stack_topleft(type) {
    var opts = {
        title: "Over Here",
        text: "Check me out. I'm in a different stack.",
        addclass: "stack-topleft",
        stack: stack_topleft
    };
    switch (type) {
        case 'error':
            opts.title = "Oh No";
            opts.text = "Watch out for that water tower!";
            opts.type = "error";
            break;
        case 'info':
            opts.title = "Breaking News";
            opts.text = "Have you met Ted?";
            opts.type = "info";
            break;
        case 'success':
            opts.title = "Good News Everyone";
            opts.text = "I've invented a device that bites shiny metal asses.";
            opts.type = "success";
            break;
    }
    $.pnotify(opts);
}

function show_stack_bottomleft(type) {
    var opts = {
        title: "Over Here",
        text: "Check me out. I'm in a different stack.",
        addclass: "stack-bottomleft",
        stack: stack_bottomleft
    };
    switch (type) {
        case 'error':
            opts.title = "Oh No";
            opts.text = "Watch out for that water tower!";
            opts.type = "error";
            break;
        case 'info':
            opts.title = "Breaking News";
            opts.text = "Have you met Ted?";
            opts.type = "info";
            break;
        case 'success':
            opts.title = "Good News Everyone";
            opts.text = "I've invented a device that bites shiny metal asses.";
            opts.type = "success";
            break;
    }
    $.pnotify(opts);
}

function show_stack_bottomright(type) {
    var opts = {
        title: "Over Here",
        text: "Check me out. I'm in a different stack.",
        addclass: "stack-bottomright",
        stack: stack_bottomright
    };
    switch (type) {
        case 'error':
            opts.title = "Oh No";
            opts.text = "Watch out for that water tower!";
            opts.type = "error";
            break;
        case 'info':
            opts.title = "Breaking News";
            opts.text = "Have you met Ted?";
            opts.type = "info";
            break;
        case 'success':
            opts.title = "Good News Everyone";
            opts.text = "I've invented a device that bites shiny metal asses.";
            opts.type = "success";
            break;
    }
    $.pnotify(opts);
}

function show_stack_custom(type) {
    var opts = {
        title: "Over Here",
        text: "Check me out. I'm in a different stack.",
        addclass: "stack-custom",
        stack: stack_custom
    };
    switch (type) {
        case 'error':
            opts.title = "Oh No";
            opts.text = "Watch out for that water tower!";
            opts.type = "error";
            break;
        case 'info':
            opts.title = "Breaking News";
            opts.text = "Have you met Ted?";
            opts.type = "info";
            break;
        case 'success':
            opts.title = "Good News Everyone";
            opts.text = "I've invented a device that bites shiny metal asses.";
            opts.type = "success";
            break;
    }
    $.pnotify(opts);
}

function show_stack_custom2(type) {
    var opts = {
        title: "Over Here",
        text: "Check me out. I'm in a different stack.",
        addclass: "stack-custom2",
        stack: stack_custom2
    };
    switch (type) {
        case 'error':
            opts.title = "Oh No";
            opts.text = "Watch out for that water tower!";
            opts.type = "error";
            break;
        case 'info':
            opts.title = "Breaking News";
            opts.text = "Have you met Ted?";
            opts.type = "info";
            break;
        case 'success':
            opts.title = "Good News Everyone";
            opts.text = "I've invented a device that bites shiny metal asses.";
            opts.type = "success";
            break;
    }
    $.pnotify(opts);
}

function show_stack_bar_top(type) {
    var opts = {
        title: "Over Here",
        text: "Check me out. I'm in a different stack.",
        addclass: "stack-bar-top",
        cornerclass: "",
        width: "100%",
        stack: stack_bar_top
    };
    switch (type) {
        case 'error':
            opts.title = "Oh No";
            opts.text = "Watch out for that water tower!";
            opts.type = "error";
            break;
        case 'info':
            opts.title = "Breaking News";
            opts.text = "Have you met Ted?";
            opts.type = "info";
            break;
        case 'success':
            opts.title = "Good News Everyone";
            opts.text = "I've invented a device that bites shiny metal asses.";
            opts.type = "success";
            break;
    }
    $.pnotify(opts);
}

function show_stack_bar_bottom(type) {
    var opts = {
        title: "Over Here",
        text: "Check me out. I'm in a different stack.",
        addclass: "stack-bar-bottom",
        cornerclass: "",
        width: "70%",
        stack: stack_bar_bottom
    };
    switch (type) {
        case 'error':
            opts.title = "Oh No";
            opts.text = "Watch out for that water tower!";
            opts.type = "error";
            break;
        case 'info':
            opts.title = "Breaking News";
            opts.text = "Have you met Ted?";
            opts.type = "info";
            break;
        case 'success':
            opts.title = "Good News Everyone";
            opts.text = "I've invented a device that bites shiny metal asses.";
            opts.type = "success";
            break;
    }
    $.pnotify(opts);
}

// event
$(function(){
    // notify basic demo
    $('#regular-notice').click(function(){
        $.pnotify({
            title: 'Regular Success',
            text: 'That thing that you were trying to do worked!',
            type: 'success'
        });
    })
    $('#sticky-notice').click(function(){
        $.pnotify({
            title: 'Sticky Notice',
            text: 'Check me out! I\'m a sticky notice. You\'ll have to close me yourself.',
            hide: false
        });
    })
    $('#transparent-notice').click(function(){
        $.pnotify({
            title: 'See Through Notice',
            text: 'No one ever pays attention to me. Why should they? I\'m practically invisible.',
            opacity: .8
        });
    })
    $('#noshadow-notice').click(function(){
        $.pnotify({
            title: 'No Shadow Notice',
            text: 'I don\'t have a shadow. (It\'s cause I\'m a vampire or something. Or is that reflections...)',
            shadow: false
        });
    })
    $('#icon-notice').click(function(){
        $.pnotify({
            title: 'Awesome Font Icon Notice',
            text: 'I have an icon that uses the awesome font icon styles.',
            icon: 'icofont-envelope-alt'
        });
    })
    $('#bootstrap-icon-notice').click(function(){
        $.pnotify({
            title: 'Bootstrap Icon Notice',
            text: 'I have an icon that uses the Bootstrap icon styles.',
            icon: 'icon-envelope'
        });
    })
                
    // notify advance demo
    $('#dyn-notice').click(function(){
        dyn_notice();
    })
    $('#nonblocking-notice').click(function(){
        $.pnotify({
            title: 'Non-Blocking Notice',
            text: 'I\'m a special kind of notice called "non-blocking". When you hover over me I\'ll fade to show the elements underneath. Feel free to click any of them just like I wasn\'t even here.\n\nNote: HTML links don\'t trigger in some browsers, due to security settings.',
            nonblock: true,
            nonblock_opacity: .2
        });
    })
    $('#style-notice').click(function(){
        $.pnotify({
            title: 'Custom Styling',
            text: 'I have an additional class that\'s used to give me special styling. I always wanted to be pretty.',
            addclass: 'custom', // see pnotify css for customing class
            icon: 'picon picon-32 picon-fill-color',
            opacity: .8,
            nonblock: true,
            nonblock_opacity: .2
        });
    })
    $('#click-notice').click(function(){
        var notice = $.pnotify({
            title: 'Click Notice',
            text: 'I wish someone would click me.'
        }).click(function(e) {
            if ($(e.target).is('.ui-pnotify-closer *, .ui-pnotify-sticker *')) return;
            notice.pnotify({
                type: 'success',
                text: 'Yay, you clicked me!<div style="text-align: center;"><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Happy_smiley_face.png/240px-Happy_smiley_face.png" /></div>'
            });
        });
    })
                
    // notify custom stacks demo
    $('#tl-notice').click(function(){
        show_stack_topleft('notice');
    })
    $('#tl-info').click(function(){
        show_stack_topleft('info');
    })
    $('#tl-success').click(function(){
        show_stack_topleft('success');
    })
    $('#tl-error').click(function(){
        show_stack_topleft('error');
    })

    $('#bl-notice').click(function(){
        show_stack_bottomleft('notice');
    })
    $('#bl-info').click(function(){
        show_stack_bottomleft('info');
    })
    $('#bl-success').click(function(){
        show_stack_bottomleft('success');
    })
    $('#bl-error').click(function(){
        show_stack_bottomleft('error');
    })

    $('#br-notice').click(function(){
        show_stack_bottomright('notice');
    })
    $('#br-info').click(function(){
        show_stack_bottomright('info');
    })
    $('#br-success').click(function(){
        show_stack_bottomright('success');
    })
    $('#br-error').click(function(){
        show_stack_bottomright('error');
    })

    $('#cr-notice').click(function(){
        show_stack_custom('notice');
    })
    $('#cr-info').click(function(){
        show_stack_custom('info');
    })
    $('#cr-success').click(function(){
        show_stack_custom('success');
    })
    $('#cr-error').click(function(){
        show_stack_custom('error');
    })

    $('#cl-notice').click(function(){
        show_stack_custom2('notice');
    })
    $('#cl-info').click(function(){
        show_stack_custom2('info');
    })
    $('#cl-success').click(function(){
        show_stack_custom2('success');
    })
    $('#cl-error').click(function(){
        show_stack_custom2('error');
    })

    $('#top-notice').click(function(){
        show_stack_bar_top('notice');
    })
    $('#top-info').click(function(){
        show_stack_bar_top('info');
    })
    $('#top-success').click(function(){
        show_stack_bar_top('success');
    })
    $('#top-error').click(function(){
        show_stack_bar_top('error');
    })

    $('#bottom-notice').click(function(){
        show_stack_bar_bottom('notice');
    })
    $('#bottom-info').click(function(){
        show_stack_bar_bottom('info');
    })
    $('#bottom-success').click(function(){
        show_stack_bar_bottom('success');
    })
    $('#bottom-error').click(function(){
        show_stack_bar_bottom('error');
    })
});