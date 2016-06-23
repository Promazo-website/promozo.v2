/**
 * Created by marc on 22/05/16.
 */
promazo.controller('homeController',function( $scope,$http,$mdToast,$timeout,AuthService, ProfileService,$mdSidenav,PodService,$mdMedia) {
    $scope.currentUser = null;
    $scope.currentPage= null;
    $scope.currentProfile=null;
    $scope.currentType=null;
    $scope.currrentBusiness=null;
    $scope.currentUniversity=null;
    $scope.currentScore=0;
    $scope.currentPods=null;

    
    AuthService.user_details()
        .then(function(data){
            $scope.setCurrentUser(data);
        });

    $scope.$watch('currentUser', function(New,Old) {
        if(New!=null) {
            PodService.get_user_pods()
                .then(function (data) {
                    $scope.currentPods = data;
                });
        }
    });
    
    $scope.$watch('currentProfile',function(New,Old){
        ProfileService.get_user_score()
            .then(function(data){
                $scope.currentScore=data;
            })
    })
    
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
    
});



