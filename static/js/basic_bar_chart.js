"use strict";

const basicBarChart = new Chart(
  $('#basic-bar-chart'),
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

