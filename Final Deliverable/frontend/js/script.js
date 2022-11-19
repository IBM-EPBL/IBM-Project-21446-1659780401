     $(document).ready(function () {
         console.log("slider init");
         // Plugin initialization
         $('.slider').slider({
            indicators: false
         });

         console.log("carousel init")
         $('.carousel').carousel();
         $('.tap-target').tapTarget('open');
         Materialize.toast('Click on articles to expand them.', 5000, '', function(){$('.tap-target').tapTarget('close');});
     })
