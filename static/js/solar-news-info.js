"use strict";

$.get(`solar_news/news_feed`, (res) => {
  // Make a bar chart with all yearly production data. 
  // console.log(res);
  // Get response from the url. 
  const status = res.status;
  const num_articles = res.totalResults;


  console.log(status);
  console.log(num_articles);

  //  const colorfulBarChart = new Chart(
  //   $('#bar-chart-compare-companies2'),
  //   {
  //     type: 'bar',
  //     data: {
  //       labels: utility_labels,
  //       datasets: [
  //         {
  //           label: 'Solar energy production (gWh)',
  //           data: production_data_list
  //         },
  //         {
  //           label: 'Total energy production/consumption (gWh)',
  //           data: consumption_data_list
  //         }
  //       ]
  //     },
  //     options: {
  //       datasets: {
  //         bar: {
  //           // We use a function to automatically set the background color of
  //           // each bar in the bar chart.
  //           //
  //           // There are many other properties that accept functions. For more
  //           // information see: https://www.chartjs.org/docs/latest/general/options.html#scriptable-options
  //           backgroundColor: () => {
  //             // `randomColor` is a JS module we found off GitHub: https://github.com/davidmerfield/randomColor
  //             // We imported it in templates/chartjs.html
  //             return randomColor();
  //           }
  //         }
  //       },
  //       scales: {
  //         // This is where you can configure x- and y-axes if you don't like the
  //         // automatic range that Chart.js sets for you.
  //         //
  //         // For more info see: https://www.chartjs.org/docs/latest/axes/cartesian/
  //         yAxes: [
  //           {
  //             ticks: {
  //               min: 0,
  //               // max: 100000000
  //             }
  //           },
  //         ]
  //       }
  //     }
  //   }
  // );
});

