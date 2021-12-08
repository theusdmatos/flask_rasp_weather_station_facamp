$(document).ready(function() {
  setInterval(function() {
    cache_clear()
  }, 300000000000000);
});

function cache_clear() {
  window.location.reload(true);
}
