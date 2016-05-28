/**
 * Created by marc on 19/05/16.
 */
promazo.factory('AuthService', function ($http, Session) {
  var authService = {};

  authService.login = function (credentials) {
    return $http
      .post('/api/core/user/login/', credentials)
      .then(function (res) {
            return   $http.get('/api/core/user/details/')
              .then(function (data) {
              Session.create(data);
              return data.data;
          });

      });
  };
    
    authService.logout = function (){
        $http.delete('/api/core/user/login/')
            .then( function () {
                this.userData=null;

            });
    };

    authService.user_details = function () {
        return $http.get('/api/core/user/details/')
            .then(function(data) {
                return data.data;
            });
    };

 
    authService.update = function (details) {
        return $http.put('/api/core/user/details/', details)
            .then(function(data) {
                return data;
            });
    };
   


   authService.reset_password = function (Email) {
       return $http.post('/api/core/user/registration/requestreset/', {'email':Email})
           };

  authService.isAuthenticated = function () {
    return !!Session.userData;
  };

  authService.register = function(formdata) {
      return $http.post('/api/core/user/registration/create/', formdata)
          .then ( function (res) {
              return res.data;
          });

  };

  return authService;
});

promazo.service('Session', function () {
  this.create = function (userData) {

    this.userData = userData;
  };
  this.destroy = function () {
    this.userData = null;
  };
});


promazo.constant('AUTH_EVENTS', {
  loginSuccess: 'auth-login-success',
  loginFailed: 'auth-login-failed',
  logoutSuccess: 'auth-logout-success',
  sessionTimeout: 'auth-session-timeout',
  notAuthenticated: 'auth-not-authenticated',
  notAuthorized: 'auth-not-authorized'
});

