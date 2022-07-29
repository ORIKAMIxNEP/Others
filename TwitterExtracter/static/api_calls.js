function search() {
  fetch(
    "http://172.31.50.223:50001/?word=" +
      document.getElementById("search").value
  ) // API呼び出し
    .then(function (data) {
      return data.json(); // json形式に変換
    })
    .then(function (TweetsData) {
      let tweet_num = document.getElementById("tweet_num").value; //ツイート数
      let tweet_fav = document.getElementById("favorite").value; //いいね数

      let tweetsHTML = ""; // HTMLに入る変数
      // let favorite="";
      for (let i = 0; i < tweet_num; i++) {
        if (TweetsData.tweets[i].favorite >= tweet_fav) {
          //指定したいいね数以上
          console.log(TweetsData.tweets[i].tweet); // ツイート
          console.log(TweetsData.tweets[i].favorite); // いいね数
          // favorite += TweetsData.tweets[i].favorite;

          //ソート
          // favorite.sort(function (a, b) {
          //     if (a > b) return -1;
          //     else if (b > a) return 1;
          //     else return 0;
          // });

          tweetsHTML +=
            "<p>" +
            TweetsData.tweets[i].tweet +
            "<br>" +
            "<br>" +
            "<h4 style=color:#FF0000>&hearts;" +
            TweetsData.tweets[i].favorite +
            "</h4>" +
            "<p>" +
            "<hr>";

          tweets.innerHTML = tweetsHTML; // HTMLに反映
        }
      }
    });
}
