function search() {
    fetch(
        "http://172.31.50.223:50001/?word=" +
        document.getElementById("search").value
    ) // API呼び出し
    .then(function (data) {
        return data.json(); // json形式で読み込む
    })
    .then(function (TweetsData) {
        let tweet_num = document.getElementById("tweet_num").value; //ツイート数を指定
        let tweet_fav = document.getElementById("favorite").value;  //いいね数を指定

        let tweetsHTML = ""; // HTMLに入れるデータの変数
        for (let i = 0; i < tweet_num; i++) {
            if(TweetsData.tweets[i].favorite >= tweet_fav) {    //指定したいいね数以上
                console.log(TweetsData.tweets[i].tweet); // ツイートの文章
                console.log(TweetsData.tweets[i].favorite); // ツイートのいいね数
                tweetsHTML += "<p>" + TweetsData.tweets[i].tweet +"<br>"+ TweetsData.tweets[i].favorite +"<p>"; // ツイートデータをHTML用データに格納
                tweets.innerHTML = tweetsHTML; // HTML用データをHTML(id:tweets)に反映
            }
        }
    });
}