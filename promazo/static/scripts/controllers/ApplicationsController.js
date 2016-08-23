/**
 * Created by marc on 8/22/16.
 */
promazo.controller('ApplicationsController',function( $scope,$log,$mdDialog,ApplicationsResource,ApplicationNotesResource,
                                             AssignedTestsResource,ApplicantTestResultsResource,
                                             ApplicationCasesResource,ApplicationCaseResultsResource,
                                             ProjectRoleResource) {

    $scope.myApplications = ApplicationsResource.query({'id':'all'});

    $scope.AvailableRoles = ProjectRoleResource.query({'id':'available'});
    
    
        
});