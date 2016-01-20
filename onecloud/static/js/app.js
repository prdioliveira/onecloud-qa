app = angular.module('onecloud.app', []);

app.controller('ServiceController', function($scope, $http){
    $scope.services = [];
    $scope.sortReverse = false;
    $scope.sortBy = '';

    $scope.order = function(attributeName){
        $scope.sortReverse = !$scope.sortReverse;
        $scope.sortBy = attributeName;
    }

    $http.get('/api/services/').success(function(data){
        $scope.services = data.results;
    });

});
