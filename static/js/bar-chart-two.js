"use strict";

// const selectedId = $('#human-id').val();

// $.get('/data_viz/', (res) => {
//     const yearlyLabels = res.labels;
//     const yearlyDatasets = res.datasets
//     });

const barChartTwo = new Chart(
  $('#bar-chart2'),
  {
    type: 'bar',
    data: {
      labels: [ new Date('2015'), new Date('2016'), new Date('2017'), new Date('2018'), new Date('2019')],
      datasets: [
        {
          label: 'Today',
          data: [{x: new Date('2016'), y: 1500}, {x: new Date('2017'), y:3600},{ x: new Date('2018'), y:2700}]
        },
        {
          label: 'Yesterday',
          data: [{ x: new Date('2016'), y:5500} , { x: new Date('2017'), y:4000} , { x: new Date('2018'), y:7300}]
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
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'year'
                }
            }],
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