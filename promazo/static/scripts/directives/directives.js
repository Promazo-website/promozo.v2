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
promazo.directive('pwdCompare', function($http, $q) {
    return {
        require: "ngModel",
        scope: {
            otherModelValue: "=pwdCompare"
        },
        link: function(scope, element, attributes, ngModel) {

            ngModel.$validators.pwdCompare = function(modelValue) {
                return modelValue == scope.otherModelValue;
            };

            scope.$watch("otherModelValue", function() {
                ngModel.$validate();
            });
        }
    };
});
