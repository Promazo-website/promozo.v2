/**
 * Created by marc on 22/05/16.
 */
promazo.controller('registerController',function( $scope,$http,$mdToast,$timeout,AuthService, ProfileService,OrgService) {
    $scope.views={stage:1,select_ornagisation:false,find_organisation:false};
    
    $scope.formdata={};
    
    $scope.registerMessage="";
    $scope.RegisterClass="";
    
    $scope.FindOrganisation = function(Email){
        OrgService.findOrganisation(Email)
          .then(function(data){
              $scope.formdata.type=data.type;
              $scope.formdata.organisation=data.organisation;
              $scope.views.find_organisation=true;
              $scope.views.select_organisation=true;
          });
          $scope.views.select_organisation=true;
    };
    
    $scope.CreateOrganisation = function(formdata) {
        if(formdata.type =='University'){
            OrgService.createUniversity(formdata.organisation_name)
                .then(function(data){
                    $scope.formdata.organisation=data;
                    $scope.views.stage=2;
                },
                function(){
                    $scope.openToast('Creation of University Failed')
                });
        };
        if(formdata.type =='Business'){
            OrgService.createBusiness(formdata.organisation_name)
                .then(function(data){
                    $scope.formdata.organisation=data;
                    $scope.views.stage=2;
                }
                ,function(){
                    $scope.openToast('Creation of Business Failed')
                });
        };

    };
    
    $scope.signup = function(formdata) {
        AuthService.register(formdata)
            .then(function() {
                $scope.registerMessage = 'Please Check your inbox for a validation email';
                $scope.registerClass = "md-primary"
            },
            function(){
                $scope.registerMessage = 'Sorry, An error has occured in signup';
                $scope.registerClass = "md-warn";
            });
    };
    
});
