/**
 * Created by marc on 28/04/16.
 */
promazo.controller( 'userController' ,['$scope','$http','$mdToast','Upload','$timeout', function( $scope,$http,$mdToast,Upload,$timeout) {

    $scope.pageview = 'home';
    $scope.errorMessages = {messages: '', status: ''};
    $scope.headers = {headers: {'X-CSRFToken': getCookie('csrftoken')}};
    $scope.editprofile=false;
    $scope.new_avatar=false;

    if ($scope.user_details==undefined) {
        $http.get('/api/core/user/details/')
            .success(function (data) {
                $scope.user_details = data;
                $scope.goto('#/user/');
                if(data.record.student_details!=undefined){
                    $scope.avatar = data.record.student_details.avatarImage;
                };
                if(data.record.business_user!=undefined){
                    $scope.avatar = data.record.business_user.avatarImage;
                };
            })
            .error(function () {
                $scope.goto('#/')
            });
    };

    $http.get('/api/core/user/documents/')
        .success(function(data){
            $scope.user_documents=data;
        });

    $scope.goto = function (url) {
        window.location.assign(url);
    };

    $scope.openToast = function (text) {
        $mdToast.show(
            $mdToast.simple()
                .textContent(text)
                .position('top left')
        );
    };

    $scope.logout=function(){
        $http.delete('/api/core/user/login')
            .success(function(){
                $scope.goto('#/');
            })

    };
    $scope.edit_profile=function(userdata) {
        $scope.userdata=userdata.record;
        if(userdata.record.business_user != undefined) {
            $scope.business_user=userdata.record.business_user
        };
        if(userdata.record.student_details != undefined) {
            $scope.student_details=userdata.record.student_details;
        };

    };

    $scope.save_profile=function(userdata,studentdata,businessdata){

        postdata={'first_name':userdata.first_name,'last_name':userdata.last_name}
        $http.put('/api/core/user/details/', postdata, $scope.headers)
            .success(function(){
                $scope.openToast('user updated');
            });
        if(studentdata !=undefined){
            postdata=studentdata;
            $http.put('/api/core/user/student/'+studentdata.id+'/', postdata, $scope.headers)
                .success(function(){
                    $scope.openToast('student profile updated');
                })
        };
        if(businessdata!=undefined){
            postdata=businessdata;
            $http.put('/api/core/user/business/'+businessdata.id+'/', postdata, $scope.headers)
                .success(function(){
                    $scope.openToast('Business User profile updated');
                })
        }

    };

    $scope.upload = function (dataUrl, name) {
        Upload.upload({
            url: '/api/core/user/avatar/',
            data: {
                file: Upload.dataUrltoBlob(dataUrl, name)
            },
        }).then(function (response) {
            $timeout(function () {
                $scope.avatar = response.data.avatar;
            });
        }, function (response) {
            if (response.status > 0) $scope.errorMsg = response.status
                + ': ' + response.data;
        }, function (evt) {
            $scope.progress = parseInt(100.0 * evt.loaded / evt.total);
        });
    };

    $scope.uploadFile = function(file,name) {
    file.upload = Upload.upload({
      url: '/api/core/user/documents/',
      data: {name: name, document: file},
    });

    file.upload.then(function (response) {
      $timeout(function () {
        file.result = response.data;
        $scope.new_avatar=false;
      });
    }, function (response) {
      if (response.status > 0)
        $scope.errorMsg = response.status + ': ' + response.data;
    }, function (evt) {
      // Math.min is to fix IE which reports 200% sometimes
      file.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
    });
    };

    $scope.deleteDoc=function(docid) {
        $http.delete('/api/core/user/documents/'+ docid+'/')
            .success(function(data){
                $scope.user_documents=data;
            })
    };

}]);
function getCookie(cname){ var name = cname + "="; var ca = document.cookie.split(';'); for(var i=0; i<ca.length; i++) { var c = ca[i]; while (c.charAt(0)==' ') c = c.substring(1); if (c.indexOf(name) == 0) return c.substring(name.length,c.length); } return ""; }
