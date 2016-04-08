var MD = ( function( $ ) {
    'use strict';

    var $fields;
    var $widgets;
    var $doc = $('document');

    $doc.ready( init );
    $.fn.mdwidget = mdwidgets;

    function init() {
        $fields = $('.md-field');
        $fields.mdwidget();
    };

    function mdwidgets() {
        if( this.length > 0 ) {
            if( cms_admin_style() === true ) {
                this.addClass('cms-admin-style')
            }
            load_help();
            for ( var i = 0; i < this.length; i++ ) {
                var $widget = $( this[ i ] );
                if( $widget.attr('id').indexOf('__prefix__') > -1 ) {
                    // do something helpful
                } else {
                    $widget.addClass('active');
                    mdwidget( $widget );
                }
            }
            $widgets = $fields.filter('.active');
        }
        return this;
    };

    function mdwidget( $widget ) {
        var widget = $widget[0];
        var $help_button = $('.md-button.help', $widget );

        $help_button.on({ click: toggle_help });
        function toggle_help( e ) {
            e.preventDefault();
            if( $widget.hasClass('show-help') ) {
                $widget.removeClass('show-help');
            } else {
                $widget.addClass('show-help');
            }
        }
        //var $help =
        //console.log ( $widget )
    }

    function load_help() {
        var url = $('.md-button.help', $fields.first() ).attr('href');
        if( url ) {
            $.ajax({ url: url, method: 'get', success: render_help });
        }
    };

    function render_help( data ) {
        var html = $( data ).filter('#mdhelp').html()
        for ( var i = 0; i < $widgets.length; i++ ) {
            var $widget = $( $widgets[ i ] );
            var $help = $('.md-help', $widget).append( html );
        }
    };

    function cms_admin_style() {
        return $('.toolbar-item').length > 0;
    };

})( django.jQuery || jQuery );
