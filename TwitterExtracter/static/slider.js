//スライダー
const range = document.getElementById("tweet_num"); //値を取得

range.addEventListener("input", (e) => {
  const value = +e.target.value;
  const label = e.target.nextElementSibling; //labelの要素を取得

  const range_width = getComputedStyle(e.target).getPropertyValue("width");
  const label_width = getComputedStyle(label).getPropertyValue("width");
  const num_width = +range_width.substring(0, range_width.length - 2);
  const num_label_width = +label_width.substring(0, label_width.length - 2);

  const max = +e.target.max; //最大値
  const min = +e.target.min; //最小値
  const left =
    value * (num_width / max) -
    num_label_width / 2 +
    scale(value, min, max, 10, -10);

  label.style.left = `${left}px`; //スタイルへ適用
  label.innerHTML = value; //labelの更新
});

// scaleの計算
const scale = (num, in_min, in_max, out_min, out_max) => {
  return ((num - in_min) * (out_max - out_min)) / (in_max - in_min) + out_min;
};
