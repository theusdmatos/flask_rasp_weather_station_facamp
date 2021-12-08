$(document).ready(function() {
  setInterval(function() {
    cache_clear()
  }, 20000);
});

function cache_clear() {
  window.location.reload(true);
}
