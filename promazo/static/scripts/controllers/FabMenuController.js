/**
 * Created by marc on 8/10/16.
 */
promazo.controller('FabMenuController',function( $scope,$timeout) {

    $scope.menu = {isOpen: false, direction: 'left', mode: 'md-fling'};
    
      $scope.$watch('menu.isOpen', function(isOpen) {
        if (isOpen) {
          $timeout(function() {
            $scope.tooltipVisible = $scope.menu.isOpen;
          }, 600);
        } else {
          $scope.tooltipVisible = $scope.menu.isOpen;
        }
      });
});