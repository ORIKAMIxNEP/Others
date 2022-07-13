function search() {
  fetch(
    "http://172.31.50.223:50001/?word=" +
      document.getElementById("search").value +
      "&?favorite=" +
      document.getElementById("favorite")
  )
    .then(function (data) {
      return data.json();
    })
    .then(function (TweetsData) {
      let tweetsHTML = "";
      for (let i = 0; i < TweetsData.tweets.length; i++) {
        console.log(TweetsData.tweets[i].tweet);
        console.log(TweetsData.tweets[i].favorite);
        tweetsHTML += "<p>" + TweetsData.tweets[i].tweet + "<p>";
        tweets.innerHTML = tweetsHTML;
      }
    });
}
