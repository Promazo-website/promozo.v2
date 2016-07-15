;(function(window, document, Darkroom) {
  'use strict';

  Darkroom.plugins['save'] = Darkroom.Plugin.extend({
    defaults: {
      callback: function(event) {
          event.preventDefault();
          /*event.preventDefault();

          var form = $('#profile_pic_form');
          $(form).find('img').attr('name', 'profile_pic');
          var data = new FormData($(form).get(0));

          $.ajax({
             url: $(this).attr('action'),
              type: $(this).attr('method'),
              data: data,
              cache: false,
              processData: false,
              contentType: false,
              success: function(data){
                  alert("Profile picture saved!");
              },
              error: function(){
                  alert("Failed saving new profile picture.");
              }
          });*/
            this.darkroom.selfDestroy();
          return false;
      }
    },

    initialize: function InitDarkroomSavePlugin() {
      var buttonGroup = this.darkroom.toolbar.createButtonGroup();

      this.destroyButton = buttonGroup.createButton({
        image: 'save'
      });

      this.destroyButton.addEventListener('click', this.options.callback.bind(this));
    },
  });
})(window, document, Darkroom);
