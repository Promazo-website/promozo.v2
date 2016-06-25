/**
 * Created by marc on 22/05/16.
 */
var promazo = angular.module('promazo', ['ngAnimate' , 'ngRoute', 'ngSanitize','ngMessages','ngMaterial','ngFileUpload', 'ngImgCrop']);

promazo.config(function ($routeProvider, $locationProvider, $httpProvider, $mdThemingProvider,$mdIconProvider) {

    $mdThemingProvider.theme('default')
        .primaryPalette('indigo')
        .accentPalette('yellow');

    $mdIconProvider
        .iconSet('Extras','/static/node_modules/mdi/mdi.svg');


    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});








