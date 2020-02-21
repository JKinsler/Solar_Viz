"use strict";

const barChart = new Chart(
  $('#bar-chart'),
  {
    type: 'bar',
    data: {
      labels: ['Watermelon', 'Canteloupe', 'Honeydew'],
      datasets: [
        {
          label: 'Today',
          data: [10, 36, 27]
        },
        {
          label: 'Yesterday',
          data: [5, 0, 7]
        }
      ]
    }
  }
);