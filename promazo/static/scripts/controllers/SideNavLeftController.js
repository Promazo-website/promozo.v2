/**
 * Created by marc on 22/05/16.
 */
promazo.controller('sideNavLeftController',function( $scope,$http,$mdToast,$timeout,$mdSidenav) {

    $scope.SideNavClose = function (SideNav) {
        $mdSidenav(SideNav).close();
    };
});