$(document).ready(function () {
    var orderByState = {
        "async": true,
        "crossDomain": true,
        "url": "http://localhost:5000/order/state",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        }
      };
      
      $.ajax(orderByState).done(function (orderByStateResponse) {
        states = []
        counts = []
        for (var i = 0; i < orderByStateResponse.length; i++) {
            states.push(orderByStateResponse[i]['_id'])
            counts.push(orderByStateResponse[i]['count'])
        }
        $('#row-1').append('<canvas id="r1-chart"></canvas>');
        var ctx = document.getElementById('r1-chart').getContext('2d');
        var options = {
            type: 'bar',
            data: {
                labels: states,
                datasets: [{
                    label: 'Orders by State',
                    data: counts,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)'
                    ],
                    borderWidth: 1,
                    borderColor: '#777',
                    hoverBorderWidth: 3,
                    hoverBorderColor: '#000'
                }]
            },
            options: {
                title: {
                    display: true,
                    fontSize: 20,
                    text: 'Orders by State'
                },
                tooltips: {
                    enabled: true
                }
            }
        }
        new Chart(ctx, options);
      });

      var orderByCity = {
        "async": true,
        "crossDomain": true,
        "url": "http://localhost:5000/order/city",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        }
      };
      
      $.ajax(orderByCity).done(function (orderByCityResponse) {
        cities = []
        counts = []
        for (var i = 0; i < orderByCityResponse.length; i++) {
            cities.push(orderByCityResponse[i]['_id'])
            counts.push(orderByCityResponse[i]['count'])
        }
        $('#row-2').append('<canvas id="r2-chart"></canvas>');
        var ctx2 = document.getElementById('r2-chart').getContext('2d');
        var options2= {
            type: 'bar',
            data: {
                labels: cities,
                datasets: [{
                    label: 'Orders by City',
                    data: counts,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)'
                    ],
                    borderWidth: 1,
                    borderColor: '#777',
                    hoverBorderWidth: 3,
                    hoverBorderColor: '#000'
                }]
            },
            options: {
                title: {
                    display: true,
                    fontSize: 20,
                    text: 'Orders by City'
                },
                tooltips: {
                    enabled: true
                }
            }
        }
        new Chart(ctx2, options2);
      });

      var orderCountsByMonth = {
        "async": true,
        "crossDomain": true,
        "url": "http://localhost:5000/order/months-count",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        }
      };


      $.ajax(orderCountsByMonth).done(function (orderCountsByMonthResponse) {
        var MONTHS = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ];
        
        counts = []
        for (var i = 0; i < orderCountsByMonthResponse.length; i++) {
            counts.push(orderCountsByMonthResponse[i]['count'])
        }

        $('#row-3').append('<canvas id="r3-chart"></canvas>');
        var ctx3 = document.getElementById('r3-chart').getContext('2d');
        var options3 = {
            type: 'line',
            data: {
                labels: MONTHS,
                datasets: [{
                    label: 'Order Count by Months',
                    data: counts,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)'
                    ],
                    borderWidth: 1,
                    borderColor: '#777',
                    hoverBorderWidth: 3,
                    hoverBorderColor: '#000'
                }
            ]
            },
            options: {
                title: {
                    display: true,
                    fontSize: 20,
                    text: 'Order Count by Months'
                },
                tooltips: {
                    enabled: true
                }
            }
        }
        new Chart(ctx3, options3);
      });


      var orderReview = {
        "async": true,
        "crossDomain": true,
        "url": "http://localhost:5000/order/reviews",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        }
      };

      $.ajax(orderReview).done(function (orderReviewResponse) {
        reviews = []
        counts = []
        for (var i = 0; i < orderReviewResponse.length; i++) {
            reviews.push(orderReviewResponse[i]['_id'])
            counts.push(orderReviewResponse[i]['count'])
        }
        $('#row-4').append('<canvas id="r4-chart"></canvas>');
        var ctx4 = document.getElementById('r4-chart').getContext('2d');
        var options4 = {
            type: 'pie',
            data: {
                labels: reviews,
                datasets: [{
                    label: 'Order Reviews',
                    data: counts,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)'
                    ],
                    borderWidth: 1,
                    borderColor: '#777',
                    hoverBorderWidth: 3,
                    hoverBorderColor: '#000'
                }]
            },
            options: {
                title: {
                    display: true,
                    fontSize: 20,
                    text: 'Order Reviews'
                },
                tooltips: {
                    enabled: true
                }
            }
        }
        new Chart(ctx4, options4);
      });

      var paymentMethods = {
        "async": true,
        "crossDomain": true,
        "url": "http://localhost:5000/payment/methods",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        }
      };

      $.ajax(paymentMethods).done(function (paymentMethodsResponse) {
        method = []
        counts = []
        for (var i = 0; i < paymentMethodsResponse.length; i++) {
            method.push(paymentMethodsResponse[i]['_id'])
            counts.push(paymentMethodsResponse[i]['count'])
        }
        $('#row-5').append('<canvas id="r5-chart"></canvas>');
        var ctx5 = document.getElementById('r5-chart').getContext('2d');
        var options5 = {
            type: 'pie',
            data: {
                labels: method,
                datasets: [{
                    label: 'Most Popular Payment Methods',
                    data: counts,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)'
                    ],
                    borderWidth: 1,
                    borderColor: '#777',
                    hoverBorderWidth: 3,
                    hoverBorderColor: '#000'
                }]
            },
            options: {
                title: {
                    display: true,
                    fontSize: 20,
                    text: 'Most Popular Payment Methods'
                },
                tooltips: {
                    enabled: true
                }
            }
        }
        new Chart(ctx5, options5);
      });

      var paymentMethodsAvg = {
        "async": true,
        "crossDomain": true,
        "url": "http://localhost:5000/payment/methods-avg",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        }
      };

      $.ajax(paymentMethodsAvg).done(function (paymentMethodsAvgResponse) {
        method = []
        avg = []
        for (var i = 0; i < paymentMethodsAvgResponse.length; i++) {
            method.push(paymentMethodsAvgResponse[i]['_id'])
            avg.push(paymentMethodsAvgResponse[i]['avg'])
        }
        $('#row-6').append('<canvas id="r6-chart"></canvas>');
        var ctx6 = document.getElementById('r6-chart').getContext('2d');
        var options6 = {
            type: 'pie',
            data: {
                labels: method,
                datasets: [{
                    label: 'Average Spent by Payment Methods',
                    data: avg,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)'
                    ],
                    borderWidth: 1,
                    borderColor: '#777',
                    hoverBorderWidth: 3,
                    hoverBorderColor: '#000'
                }]
            },
            options: {
                title: {
                    display: true,
                    fontSize: 20,
                    text: 'Average Spent by Payment Methods'
                },
                tooltips: {
                    enabled: true
                }
            }
        }
        new Chart(ctx6, options6);
      });


      var productCategories = {
        "async": true,
        "crossDomain": true,
        "url": "http://localhost:5000/product/categories",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        }
      };

      $.ajax(productCategories).done(function (productCategoriesResponse) {
        method = []
        counts = []
        for (var i = 0; i < productCategoriesResponse.length; i++) {
            method.push(productCategoriesResponse[i]['_id'])
            counts.push(productCategoriesResponse[i]['count'])
        }
        $('#row-7').append('<canvas id="r7-chart"></canvas>');
        var ctx7 = document.getElementById('r7-chart').getContext('2d');
        var options7 = {
            type: 'pie',
            data: {
                labels: method,
                datasets: [{
                    label: 'Most Popular Product Categories',
                    data: counts,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)'
                    ],
                    borderWidth: 1,
                    borderColor: '#777',
                    hoverBorderWidth: 3,
                    hoverBorderColor: '#000'
                }]
            },
            options: {
                title: {
                    display: true,
                    fontSize: 20,
                    text: 'Most Popular Product Categories'
                },
                tooltips: {
                    enabled: true
                }
            }
        }
        new Chart(ctx7, options7);
      });
});