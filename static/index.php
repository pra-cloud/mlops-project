<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>intoduction</title>

    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css2?family=Arvo&display=swap" rel="stylesheet">
      <style>
      body{
      background: url(switzerland-5214914_1920.jpg) center center fixed;
        background-size:cover;
          text-align: center;
          font-family: 'Arvo',serif;
          }
	.pm{
	
	letter-spacing:2.5px;
	}
	.km{
	color:white;
	}
	.jumbotron{
	background-color:transparent;
	}
	h1:hover{
	color:black;
	}
          .ktm{
              width:500px;
              height:900px;
              margin-left:400px;
              margin-top: 20px;
          }
	</style>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
      
      <!-- facebook api-->
      
      <div id="fb-root"></div>
<script async defer crossorigin="anonymous" src="https://connect.facebook.net/en_GB/sdk.js#xfbml=1&version=v7.0" nonce="goH59522"></script>
      
      
      
      <div class="container-fluid">
   <div class="pm"> 
<div class="km"><h1>Welcome to on my contact page</h1>
</div>
</div>
<div class="jumbotron">
<form class="form-horizontal">
 <div class="form-group">
<div class="col-xs-offset-2 col-xs-8">
<input type="email" id="email" placeholder="your Email" class="form-control">


</div>
</div>
</form>


<div class="form-group">
<div class="col-xs-offset-3 col-xs-6">
<input type="submit" id="submit" value="suscribe" class="btn btn-info btn-lg">
</div>
</div>

</div>
<div class="row>">
    <!--facebbok api button-->
      <div class="col-sm-offset-3 col-sm-2">
          <div class="fb-like" data-href="http://prateek.offyoucode.co.uk" data-width="" data-layout="button_count" data-action="like" data-size="small" data-share="true"></div>
    
    </div>
    
    <div class="col-sm-2">
    
    </div>
      
    
     <div class="col-sm-2">
         
         
<a class="twitter-share-button"
  href="https://twitter.com/intent/tweet?text=Hello%20world"
  data-size="small">
Tweet</a>

    
    </div>
        
    </div> 
<div>
    <a class="twitter-timeline"
  href="https://twitter.com/TwitterDev"
  data-tweet-limit="3"
 data-height="600"
        data-width="600"
 data-chrome="">
Tweets by @TwitterDev
               </a>
          </div>
      </div>
      
      
      <script>window.twttr = (function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0],
    t = window.twttr || {};
  if (d.getElementById(id)) return t;
  js = d.createElement(s);
  js.id = id;
  js.src = "https://platform.twitter.com/widgets.js";
  fjs.parentNode.insertBefore(js, fjs);

  t._e = [];
  t.ready = function(f) {
    t._e.push(f);
  };

  return t;
}(document, "script", "twitter-wjs"));</script>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>