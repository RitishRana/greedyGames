var module = angular.module("sampleapp", ['ngRoute']);
module.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})
module.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

module.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
            }).
            when('/tracks', {
                templateUrl: '/static/angularapp/html/tracks.html',
                controller: 'tracksController'
            }).
            when('/genres', {
                templateUrl: '/static/angularapp/html/genres.html',
                controller: 'genreController'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);

module.controller("tracksController", function($scope, $http, $window) {
    $http.get('/tracks').then(
        function(data){
            $scope.tracks = data.data.tracks;
        }
    );

    $scope.open = function(id) {
                    $scope.id = id;
                    $http.get('/track/'+ $scope.id).then(
                    function(data){
                        $scope.trackDetail = data.data;
                    });
                };

    $scope.search = function(text) {
                    console.log(text);
                    $http.get('/track/search/'+ text).then(

                    function(data){
                        $scope.tracks = data.data.tracks;
                    });
                };

    $scope.addNewTrack = function() {
                    $scope.genreClick = "genre";
                    $scope.newTrack = {};
                    $http.get('/genres/').then(
                    function(data){
                        $scope.genres = data.data;
                    });
                };

    $scope.click = function(name, id) {
                    $scope.genreClick = name;
                    $scope.newTrack.genre_id = id;
                };
    $scope.add = function(obj) {
                    $http.post('/track/add/', obj).then(
                    function(data){
                        $window.location.reload();
                    });
                };
});
module.controller("genreController", function($scope, $http, $window) {
    $scope.data = {};
    $http.get('/genres').then(
        function(data){
            $scope.genres = data.data;
        }
    );

    $scope.editGenre = function(name, id) {
                    $http.get('/genre/edit/'+ name + "/" + id).then(
                    function(data){
                        $window.location.reload();
                    });
                };

    $scope.open = function(name, id) {
                   $scope.genreName = name;
                   $scope.id = id;
                };

    $scope.addNewGenre = function(newName) {
                    $http.get('/genre/add/'+ newName).then(
                    function(data){
                        $window.location.reload();
                    });
                };

});
