"use strict";

const year = $('#production-consumption').data('year');
console.log(year);

$.get(`/data_viz/${year}/compare_companies`, (res) => {
  // Make a bar chart with all yearly production data. 
  console.log(res);
  // Get utilities list. 
  const utility_labels = res.labels_utilities;
  // Get production data that corresponds with each company
  const production_data_list = res.year_productions;
  const consumption_data_list = res.year_consumptions;

  console.log(utility_labels)
  console.log(production_data_list)
  console.log(consumption_data_list)

   const colorfulBarChart = new Chart(
    $('#bar-chart-compare-companies2'),
    {
      type: 'bar',
      data: {
        labels: utility_labels,
        datasets: [
          {
            label: 'Solar energy production (gWh)',
            data: production_data_list
          },
          {
            label: 'Total energy consumption (gWh)',
            data: consumption_data_list
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
                // max: 100000000
              }
            },
          ]
        }
      }
    }
  );
});

