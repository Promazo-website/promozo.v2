/**
 * Created by marc on 25/06/16.
 */
promazo.controller( 'validationController' , function( $scope,$http,AuthService){
    $scope.pageview='home';

    AuthService.validate($scope.DateHash,$scope.UserHash)
                .then(function(data){
                    $scope.pageview='setpassword';
                },
                function() {
                    $scope.pageview='badValidation';
                })
                




    $scope.setPassword = function(formdata) {
        AuthService.setPassword($scope.DateHash,$scope.UserHash,formdata)
            .then(function(data) {
                $scope.pageview='passwordset';
            },function(error){
                $scope.pageview='error-contact';
            });

    };
    $scope.goto=function(url){
        window.location.assign(url);
    };
});