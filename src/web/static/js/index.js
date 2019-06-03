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
        $('#col-1').append('<canvas id="c1-chart"></canvas>');
        var ctx = document.getElementById('c1-chart').getContext('2d');
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
                    fontSize: 25
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
        cities_counts = []
        for (var i = 0; i < orderByCityResponse.length; i++) {
            cities.push(orderByCityResponse[i]['_id'])
            cities_counts.push(orderByCityResponse[i]['count'])
        }
        $('#col-3').append('<canvas id="c3-chart"></canvas>');
        var ctx2 = document.getElementById('c3-chart').getContext('2d');
        var options2= {
            type: 'bar',
            data: {
                labels: cities,
                datasets: [{
                    label: 'Orders by City',
                    data: cities_counts,
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
                    fontSize: 25
                },
                tooltips: {
                    enabled: true
                }
            }
        }
        new Chart(ctx2, options2);
      });

      var orderMinMax = {
        "async": true,
        "crossDomain": true,
        "url": "http://localhost:5000/order/min-max",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        }
      };
      
      $.ajax(orderMinMax).done(function (orderMinMaxResponse) {
        $('#col-2').append('<canvas id="c2-chart"></canvas>');
        var ctx2 = document.getElementById('c2-chart').getContext('2d');
        var options2= {
            type: 'bar',
            data: {
                labels: ['Min', 'MAX'],
                datasets: [{
                    label: 'Min and Max ',
                    data: [orderMinMaxResponse['min'], orderMinMaxResponse['max']],
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
                    fontSize: 25
                },
                tooltips: {
                    enabled: true
                }
            }
        }
        new Chart(ctx2, options2);
      });
});