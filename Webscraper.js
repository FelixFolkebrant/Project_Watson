const request = require('request')
const cheerio = require('cheerio')

request('https://cloud.timeedit.net/abbindustrigymnasium/web/public1/ri1Y7X3QQQfZY6QfZ5073515y7Y7.html', (error, response, html) => {
      if(!error && response.statusCode == 200){
            const $ = cheerio.load(html);
            
            const weekdiv = $('.c  col1');

            console.log(weekdiv);

            // const output = weekdiv.children('')next().text();

            // console.log(output);
      }
});
