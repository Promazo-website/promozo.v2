/**
 * Created by marc on 23/05/16.
 */
promazo.controller('updateUserController',function( $scope,$http,$mdToast,$timeout,AuthService, ProfileService, SkillsService, Upload) {

    $scope.formdata = $scope.currentProfile;

    SkillsService.list()
        .then(function(data){
            $scope.skills = data;
        })

    SkillsService.assigned()
        .then(function(data){
            $scope.userskills = data;
        })
    $scope.updateUser = function(data) {
        AuthService.update(data)
            .then(function(data){
                $scope.openToast('User Updated');
                $scope.SideNavOpen('right');
            });
    };

    $scope.toggle = function (item, list) {
        found=-1;

        for(items in list) {
            if(list[items].name == item.name) {
                found=items;
            };
        };

         if (found > -1) {
          list.splice(found, 1);
          SkillsService.unassign(item)
             .then(function(data){
                 SkillsService.assigned()
                     .then(function(data){
                         $scope.userskills=data;
                     });
             });
         }
         else {
            list.push(item);
            SkillsService.assign(item)
                .then(function(data){
                    SkillsService.assigned()
                        .then(function(data){
                            $scope.userskills=data;
                        });
                });
         };
    };


    $scope.exists = function (item, list) {
        found=false;

        for(items in list) {
            if(list[items].name == item.name) {
                found=true;
            };
        };
        return found;
    };


    $scope.addNew = function(newSkill) {
        SkillsService.new({name:newSkill})
            .then(function(data){
                SkillsService.assigned()
                    .then(function(data) {
                        $scope.userskills=data;
                    });
                SkillsService.list()
                    .then(function(data){
                        $scope.skills=data;
                    });
            });
    };

     $scope.cropimage = function(){
        $scope.cropper = {};
        $scope.cropper.sourceImage = $scope.formdata.avatarImage;
        $scope.cropper.croppedImage   = null;
        $scope.bounds = {};
        $scope.bounds.left = 10;
        $scope.bounds.right = 150;
        $scope.bounds.top = 150;
        $scope.bounds.bottom = 10;
    };

    $scope.saveCroppedImage = function(new_image) {
        $scope.formdata.avatarImage=new_image;
        $scope.file=new_image;
        $scope.uploadAvatar();
    };

    $scope.avatarUpload = function (dataUrl, name) {

        Upload.upload({
            url: '/api/core/user/avatar/',
            data: { file: Upload.dataUrltoBlob(dataUrl, name) }

        }).then(function (response) {
            $scope.formcounter+=1;
            ProfileService.update_profile(postdata)
                .then(function(data){
                    $scope.setCurrentProfile(data);
                });
        });
    };



});