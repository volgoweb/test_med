
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

    $scope.week_date_from = new Date();

    this.get_week_date_from_str = function() {
        var day = $scope.week_date_from.getDate();
        var month = $scope.week_date_from.getMonth() + 1;
        var year = $scope.week_date_from.getFullYear();
        return day + "." + month + "." + year;
    }

    this.updateWeek = function() {
        $http
            .get(app.get_week_days_url + '?doctor=' + $scope.record.doctor + '&date_from=' + controller.get_week_date_from_str())
            .success(function(data) {
            $scope.days = data;
            app.$choose_dt_col.show();
        });
    };

    this.book = function(datetime_str) {
        $('#booking-form-fields').modal('show');
        $scope.record.datetime = datetime_str;
        $('#id_datetime').val($scope.record.datetime);
        $scope.bookingForm.$setPristine();
    }

    this.prevWeek = function() {
        $scope.week_date_from = new Date($scope.week_date_from.getTime() - 7 * 24 * 60 * 60 * 1000);
        controller.updateWeek();
    }

    this.nextWeek = function() {
        $scope.week_date_from = new Date($scope.week_date_from.getTime() + 7 * 24 * 60 * 60 * 1000);
        controller.updateWeek();
    }
});
