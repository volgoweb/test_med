
var app = angular.module('booking', []);
app.base_url = '/booking/';
app.get_week_days_url = app.base_url + 'get-days-for-booking/';

app.controller('chooseDateTime', function($scope, $http) {
    var controller = this;
    $scope.record = {
        datetime: '',
        doctor: '',
    };
    app.$choose_dt_col = $('.book__choose-dt-col');
    app.$choose_dt_col.hide();

    this.updateWeek = function() {
        $http.get(app.get_week_days_url + '?doctor=' + $scope.record.doctor).success(function(data) {
            $scope.days = data;
            app.$choose_dt_col.show();
        });
    };

    this.book = function(datetime_str) {
        $('#booking-form-fields').modal('show');
        $scope.record.datetime = datetime_str;
        $('#id_datetime').val($scope.record.datetime);
        // $scope.change();
        $scope.bookingForm.$setPristine();
        console.log($scope.record.datetime);
        console.log($('#id_datetime').val());
    }
});
