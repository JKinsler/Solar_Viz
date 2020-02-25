// THIS CODE DOESN'T WORK

"use strict";

const timeFormat = 'YYYY';

  const barChart4 = new Chart(
    $('#bar-chart4'),
    {
      type: 'bar',
      data: [{x:'2016-12-25', y:20}, 
            {x:'2017-12-25', y:20},
            {x:'2018-12-25', y:20},
            {x:'2019-12-25', y:20}],
      options: {
        scales: {
          xAxes: [{
            type: 'time',
            time: {
              unit: 'year'
             
            }
          }]
        },
        // tooltips: {
        //   callbacks: {
        //     title: (tooltipItem) => {
        //       return moment(tooltipItem.label).format('YYYY')
        //     }
        //   }
        // }
      }
    }
  );