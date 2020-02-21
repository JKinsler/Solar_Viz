// Make a function that lists production by year

// Debugging helpers:
// .load list_production_by_year.js
// listProductionByYear(exampleDict)


"use strict";


const listProductionByYear = (productionByYearDict) => {
    //List all production by year 
    
    // print the exampleDict to the console
    console.log(exampleDict);

    // print the exampleDict keys and values to the console
    for (const year in exampleDict) {
        console.log(year); 
        console.log(exampleDict[year]);
    };

    console.log('just ran the function: listProductionByYear');
};

// notes with Marisa: can use Ajax example as shown below with GET / POST method

// $.get('/yearly-production-data', (res) => {
//     for (r in res){
//         $('#YPT').append(`<tr><td>${r.year}</td><td>${r.production}</td></tr>`)
//     }
    
// })

// create an example dictionary to use as an input parameter in the function
// when testing.
const exampleDict = {
    2007 : 7000,
    2008 : 8000,
    2009 : 9000,
};



//Get a value from exampleDict:
// > exampleDict[2007]
// 7000
// >

