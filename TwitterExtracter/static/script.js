fetch("http://172.31.50.223:50001/") // API呼び出し
  .then(function (data) {
    return data.json(); // json形式で読み込む
  })
  .then(function (TweetsData) {
    let tweetsHTML = ""; // HTMLに入れるデータの変数
    for (let i = 0; i < TweetsData.tweets.length; i++) {
      console.log(TweetsData.tweets[i].tweet); // ツイートの文章
      console.log(TweetsData.tweets[i].favorite); // ツイートのいいね数
      tweetsHTML += "<p>" + TweetsData.tweets[i].tweet + "<p>"; // ツイートデータをHTML用データに格納
      tweets.innerHTML = tweetsHTML; // HTML用データをHTML(id:tweets)に反映
    }
  });
