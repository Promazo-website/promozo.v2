var promazo = angular.module('promazo', ['ngAnimate' , 'ngRoute', 'ngSanitize','ngMessages','ngMaterial']);

promazo.config(function ($routeProvider, $locationProvider, $httpProvider) {

    $routeProvider
        .when('/', {
            templateUrl: '/static/snippets/home.html',
            controller: 'baseController'
        })
        .when('/student/', {
            templateUrl: '/static/snippets/student/home.html',
            controller: 'baseController'
        })
        .when('/validate/:code1/:code2/', {
            templateUrl: '/static/snippets/validate.html',
            controller: 'validateController',
            resolve:{parms:'$routeParams',type:function(){return 'validate';}}
        })
        .otherwise({
            redirectTo: '/'
        });
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

promazo.directive('usernameValidator', function($http, $q) {
    return {
        require: 'ngModel',
        link: function(scope, element, attrs, ngModel) {
            ngModel.$asyncValidators.username = function(modelValue, viewValue) {
                return $http.get('/api/core/user/registration/username/?username=' + viewValue)
                    .success(function(){
                        return true;
                    }

                );
            };
        }
    };
});

promazo.directive('emailValidator', function($http, $q) {
    return {
        require: 'ngModel',
        link: function(scope, element, attrs, ngModel) {
            ngModel.$asyncValidators.validemail = function(modelValue, viewValue) {
                return $http.get('/api/core/user/registration/email/?email=' + viewValue)
                    .success(function(){
                        return true;
                    }

                );
            };
        }
    };
});

promazo.controller('base', function($scope,$http,$mdToast){

});


promazo.controller( 'baseController' , function( $scope,$http,$mdToast){

    $scope.pageview = 'home';
    $scope.errorMessages={messages:'',status:''};
    $scope.headers={ headers: { 'X-CSRFToken': getCookie('csrftoken') }} ;

    if(!$scope.user_details) {
        $http.get('/api/core/user/details/')
            .success(function(data) {
                $scope.user_details=data;
                $scope.goto('#/student/');
            })
            .error(function(){
                $scope.goto('#/')
            });
    }

    $scope.goto=function(url){
        window.location.assign(url);
    };

    $scope.openToast = function(text) {
      $mdToast.show(
          $mdToast.simple()
          .textContent(text)
          .position('top left')
      );
    };

    $scope.login=function(formdata){
        $http.post('/api/core/user/login/', formdata, $scope.headers)
            .success(function(data) {
                $scope.user_details=data
                $scope.goto('#/student/');
                })
            .error( function(data,status) {
                $scope.errorMessages.messages=data;
                $scope.errorMessages.status=status;
                $scope.openToast(data);
            })

    };

    $scope.logout=function(){
        $http.delete('/api/core/user/login')
            .success(function(){
                $scope.goto('#/');
            })

    };

    $scope.forgot_password=function(formdata) {
        $http.post('/api/core/user/registration/requestreset/',{email:formdata.email}, $scope.headers)
            .success(function(){
                $scope.pageview='reset-email-sent';
            })
            .error(function(){
                $scope.pageview='error-contact';
            })
    };

    $scope.signup = function(formdata) {
        $http.post('/api/core/user/registration/create/', formdata, $scope.headers)
            .success(function() {
                $scope.pageview = 'registration-email-sent';
            })
            .error(function(){
                $scope.pageview='error-contact';
            });
    };
});

promazo.controller( 'validateController' , function( $scope,$http,$mdToast){
    $scope.pageview='home';

    $scope.setPageView = function(resolve) {
        $scope.code1=resolve.parms.code1;
        $scope.code2=resolve.parms.code2;
        $scope.type=resolve.type;

        $http.post('/api/core/user/registration/verify/'+ $scope.code2 +'/'+$scope.code1+'/')
            .success(function() {
                $scope.pageview='setpassword';
            })
            .error(function(){
                $scope.pageview='badValidation';
            });

    };

    $scope.goto=function(url){
        window.location.assign(url);
    };

});



function getCookie(cname){ var name = cname + "="; var ca = document.cookie.split(';'); for(var i=0; i<ca.length; i++) { var c = ca[i]; while (c.charAt(0)==' ') c = c.substring(1); if (c.indexOf(name) == 0) return c.substring(name.length,c.length); } return ""; }