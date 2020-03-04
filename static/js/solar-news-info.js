"use strict";

$.get(`solar_news/news_feed`, (res) => {
  // Make a bar chart with all yearly production data. 
  // console.log(res);
  // Get response from the url. 
  const status = res.status;
  const num_articles = res.totalResults;
  const title = res[articles](0)[title]


  console.log(status);
  console.log(num_articles);

  $('#total_articles').text(num_articles);

});

