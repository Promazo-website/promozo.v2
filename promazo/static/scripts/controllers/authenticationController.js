/**
 * Created by marc on 22/05/16.
 */
promazo.controller('authenticationController',function( $scope,$rootScope,$http,$mdToast,$timeout,AUTH_EVENTS, AuthService) {

    $scope.ani_classes={pr1:'',pr2:'',pr3:'',pr4:'',pr5:'',pr6:'',pr7:'',pr8:''};    
   
    $scope.credentials = {
        username: '',
        password: '',
        error: false,
        error_message: null,
    };
    
    $scope.register_form = {
        username: '',
        password1: '',
        password2: '',
        email:'',
        error: false,
        error_message: null,
        completed:false,
    };

    $scope.resetMessage=null;
    $scope.resetClass=null;
    
    $scope.setCurrentPage('login-page');
    
    $scope.openToast = function(text) {
      $mdToast.show(
          $mdToast.simple()
          .textContent(text)
          .position('top left')
      );
    };
    

    $scope.login = function(credentials) {

    AuthService.login(credentials).then(function (user) {
     $rootScope.$broadcast(AUTH_EVENTS.loginSuccess);
      $scope.setCurrentUser(user);
    }, function (data) {
        $scope.openToast('Login Failed:' + data.non_field_errors);
        credentials.error=true;
        credentials.error_message=data.data;
      $rootScope.$broadcast(AUTH_EVENTS.loginFailed);
    });
  };
    
    $scope.register = function (register_form) {
        AuthService.register(register_form)
            .then( function () {
                register_form.completed = true;
                
            })
            .error( function (data) {
                register_form.error=true;
                register_form.error_message = data.data;
                
            });
        
    };
    
    

    $scope.logout = function() {
        AuthService.logout();
        $scope.deleteCurrentUser();
        $scope.goto('/');
    };
    

    $scope.forgot_password=function(email) {
        AuthService.reset_password(email)
            .success(function(){
                $scope.resetMessage="reset request successful! Please check your inbox for a reset email";
                $scope.resetClass='md-primary'
            })
            .error(function(){
                $scope.resetMessage='Sorry, there was a problem. Your email was not recognised';
                $scope.resetClass = "md-warn"
            })
    };


    $scope.addclasses=function (item) {
        if(item=='') {
            return 'show_info animated fadeIn'
        } else {
            return ''
        }
    };

    $scope.toggleProjects = function(item) {
        
        if(item==1) {
            $scope.ani_classes.pr1 = $scope.addclasses($scope.ani_classes.pr1);
        } 
        if(item==2) {
            $scope.ani_classes.pr2 = $scope.addclasses($scope.ani_classes.pr2);
        } 
        if(item==3) {
            $scope.ani_classes.pr3 = $scope.addclasses($scope.ani_classes.pr3);
        }         
        if(item==4) {
            $scope.ani_classes.pr4 = $scope.addclasses($scope.ani_classes.pr4);
        }  
        if(item==5) {
            $scope.ani_classes.pr5 = $scope.addclasses($scope.ani_classes.pr5);
        }
        if(item==6) {
            $scope.ani_classes.pr6 = $scope.addclasses($scope.ani_classes.pr6);
        }  
        if(item==7) {
            $scope.ani_classes.pr7 = $scope.addclasses($scope.ani_classes.pr7);
        }  
        if(item==8) {
            $scope.ani_classes.pr8 = $scope.addclasses($scope.ani_classes.pr8);
        }  
    }

});