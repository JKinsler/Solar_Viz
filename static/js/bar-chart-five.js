"use strict";


$.get('/data_viz/all_production', (res) => {
  // Make a bar chart with all yearly production data. 

  // Get years of production. 
  const yearly_labels = res.labels_by_year;
  // Get production data that corresponds with each year
  const yearly_datasets_list = res.yearly_datasets;

  // Create a chart 
  const barChartFive = new Chart(
  $('#bar-chart2'),
  {
    type: 'bar',
    data: {
      labels: yearly_labels,
      datasets: [
        {
          label: 'Annual Solar Energy Generation (GWh)',
          data: yearly_datasets_list
        },
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
              max: 200
            }
          },
        ]
        }
    }
  }
);
});


