"use strict";

const showArticles = (articles) => {
  for (const article of articles){
    const title = article.title;
    const source = article.source.name;
    const published = article.publishedAt;
    const description = article.description;
    const articleUrl = articles.url;
    const imageUrl = article.urlToImage;
    
    // console.log(title);

    // $('#article_url').append(
      // `<a href=${articleUrl}>`'</a>'
    // );

    $('#article_image').append(
      `<img src=${imageUrl}`
      );

    $('#news_articles').append(
      '<li class=title>'+ title +'</li>'
      + '<ul class=source>' + source + '</ul>'
      + '<ul class=source>' + published + '</ul>'
      + '<ul class=description>' + description + '</ul>'
      // + '<ul class=link>' +  + '</ul>'
    );
  }
};


$.get(`solar_news/news_feed`, (res) => {
  // Make a bar chart with all yearly production data. 
  // console.log(res);
  // Get response from the url. 
  const status = res.status;
  const num_articles = res.totalResults;

  // variables that will repeat for each article:
  const title = res.articles[0].title;
  const source = res.articles[0].source.name;
  const published = res.articles[0].publishedAt;
  const description = res.articles[0].description;
  const articleUrl = res.articles[0].url;
  const imageUrl = res.articles[0].urlToImage;
  const resArticles = res.articles


  console.log(status);
  console.log(num_articles);
  console.log(title);
  console.log(source);
  console.log(published);
  console.log(description);
  console.log(articleUrl);
  console.log(imageUrl);
  console.log(resArticles)


  $('#total_articles').text(num_articles);

  showArticles(resArticles);
});

