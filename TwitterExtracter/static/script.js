function search() {
  fetch(
    "http://172.31.50.223:50001/?word=" +
      document.getElementById("search").value
  )
    .then(function (data) {
      return data.json();
    })
    .then(function (TweetsData) {
      let tweetsLimit = document.getElementById("tweetsLimit").value;
      let favoriteLimit = document.getElementById("favorite").value;
      let tweetsHTML = "";
      for (let i = 0; i < tweetsLimit; i++) {
        if (TweetsData.tweets[i].favorite >= favoriteLimit) {
          console.log(TweetsData.tweets[i].tweet);
          console.log(TweetsData.tweets[i].favorite);
          tweetsHTML +=
            "<p>" +
            TweetsData.tweets[i].tweet +
            "<br>❤ " +
            TweetsData.tweets[i].favorite +
            "<p>";
          tweets.innerHTML = tweetsHTML;
        }
      }
    });
}
