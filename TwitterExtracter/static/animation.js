//読み込み完了後の処理
function btn_click() {
  //ローディング
  const loaded = document.querySelector(".loading");
  loaded.style.visibility = "visible";
  const tweets_content = "-visible";
  const $target = $(".bg");
  let count = 0;
  const countUp = () => {
    const timeoutId = setTimeout(countUp, 1000);
    count++;
    if (count > 3) {
      $target.addClass(tweets_content);
      $target.removeClass(tweets_content);
      const loaded = document.querySelector(".loading");
      loaded.classList.add(".loaded");
      const t_content = document.querySelector(".tweets_content");
      t_content.style.visibility = "visible";
      loaded.style.visibility = "hidden";
      clearTimeout(timeoutId); //timeoutIdをclearTimeoutで指定している
    }
  };
  countUp();
}
