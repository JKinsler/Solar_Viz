"use strict";

const barChart3 = new Chart(
  $('#bar-chart3'),
  {
    type: 'bar',
    data: {
      labels: ['2008', '2009', '2010'],
      datasets: [
        {
          label: 'total solar production',
          data: [5000, 7000, 8000]
        }
      ]
    },
    options: {
      datasets: {
        bar: {
          // We use a function to automatically set the background color of
          // each bar in the bar chart.
          //
          // There are many other properties that accept functions. For more
          // information see: https://www.chartjs.org/docs/latest/general/options.html#scriptable-options
          backgroundColor: () => {
            // `randomColor` is a JS module we found off GitHub: https://github.com/davidmerfield/randomColor
            // We imported it in templates/chartjs.html
            return randomColor();
          }
        }
      },
      scales: {
        // This is where you can configure x- and y-axes if you don't like the
        // automatic range that Chart.js sets for you.
        //
        // For more info see: https://www.chartjs.org/docs/latest/axes/cartesian/
        yAxes: [
          {
            ticks: {
              min: 0,
              max: 10000
            }
          },
        ]
      }
    }
  }
);
