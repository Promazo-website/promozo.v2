/**
 * Created by marc on 22/05/16.
 */
promazo.controller('authenticationController',function( $scope,$rootScope,$http,$mdToast,$timeout,AUTH_EVENTS, AuthService) {
    
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

});