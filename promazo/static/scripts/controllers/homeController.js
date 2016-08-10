/**
 * Created by marc on 22/05/16.
 */
promazo.controller('homeController',function( $scope,$http,$mdToast,$timeout,AuthService, ProfileService,$mdSidenav,$mdMedia) {
    $scope.currentUser = null;
    $scope.currentPage= 'home';
    $scope.currentProfile=null;
    $scope.currentType=null;
    $scope.currrentBusiness=null;
    $scope.currentUniversity=null;
    $scope.currentScore=0;
    $scope.callType=null;
    $scope.DateHash=null;
    $scope.UserHash=null;
    $scope.micrositePage='sign-in';

    $scope.setMicrositePage = function (page) {
        $scope.micrositePage=page;
        
    };
    AuthService.user_details()
        .then(function(data){
            $scope.setCurrentUser(data);
        });

    $scope.$watch('currentProfile',function(New,Old){
        ProfileService.get_user_score()
            .then(function(data){
                $scope.currentScore=data;
            })
    });

    $scope.blankCallType = function () {
        $scope.callType=null;
        $scope.goto('/');
    };
    
    $scope.setCurrentUser = function (user) {
        if (user==null){
            return $scope.deleteCurrentUser();
        };
        $scope.currentUser=user.record;
        $scope.currentType=user.user_type;
        if(user.record.University.length){
            $scope.currentUniversity=user.record.University[0];
            $scope.currentProfile=user.record.student_details;
        }else{
            if(user.record.Business.length){
                $scope.currerntBusiness=user.record.Business[0];
                $scope.currentProfile=user.record.business_user;
            };
        };

    };
    
    $scope.updateCurrentUser = function(){
        AuthService.user_details()
            .then(function(data){
                $scope.setCurrentUser(data);
            })
    };
    
    $scope.deleteCurrentUser = function(){
        $scope.currentUser=null;
        $scope.currentType=null;
        $scope.currentUniversity=null;
        $scope.currentBusiness=null;
        $scope.currentProfile=null;
    };
    
    $scope.setCurrentPage = function (page) {
        $scope.currentPage = page;
    };
    
    $scope.getCurrentProfile = function () {
        return $scope.currentProfile;
    };
    
    
    $scope.setCurrentProfile = function (profile) {
        $scope.currentProfile=profile;
        $scope.currentProfile.dob = new Date($scope.currentProfile.date_of_birth);
        
    };
    
    $scope.setCurrentScore = function (score) {
        $scope.currentScore = score;
    };

    
    $scope.logout = function() {
        AuthService.logout();
        $scope.setCurrentUser(null);
        $scope.goto('/');
    };

    $scope.currentScoreClass="";
    
    if ($scope.currentScore < 40) {
        $scope.currentScoreClass='md-accent';
    };
    if($scope.currentScore < 20) {
        $scope.currentScoreClass = 'md-warn';
    };

    $scope.openToast = function(text) {
      $mdToast.show(
          $mdToast.simple()
          .textContent(text)
          .position('top left')
      );
    };
    
    
    $scope.SideNavOpen = function(SideNav) {
        $mdSidenav(SideNav).open();
    };

    $scope.goto=function(url){
        window.location.assign(url);
    };
});



