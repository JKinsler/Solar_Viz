"use strict";

const barChart = new Chart(
  $('#bar-chart'),
  {
    type: 'bar',
    data: {
      labels: ['Watermelon', 'Canteloupe', 'Honeydew'],
      datasets: [
        {
          label: 'total production',
          data: [25, 36, 27]
        }
      ]
    }
  }
);

