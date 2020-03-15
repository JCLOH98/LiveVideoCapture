<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<meta name="author" content="JCLOH">
<title>Live Streaming Webcam</title>
</head>

<header>
  <h1>Live Streaming Webcam</h1>
</header>

<style media="screen">
  nav{text-align: center;}
  h1{text-align: center;}
  p{text-align: center;}
  table,tr,th,td{margin:auto; border: 2px solid black; border-collapse: collapse; table-layout: fixed; width: 100px;}
  th{text-align: center; padding: 5px 10px 5px 10px;}
</style>

<body>
  <p>
  <img src="{{ url_for('video_feed') }}">
  </p>
</body>
<footer>
</footer>

</html>

