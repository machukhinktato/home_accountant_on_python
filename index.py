from variables import CONNECTION_OK

def index_view():
    index = """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>
                Financial Keeper
                </title>
                <!-- Latest compiled and minified CSS -->
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
                <!-- Optional theme -->
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap-theme.min.css"
                      integrity="sha384-6pzBo3FDv/PJ8r2KRkGHifhEocL+1X2rVCTTkUfGk7/0pbek5mMa1upzvWbrUbOZ" crossorigin="anonymous">

                <!-- Latest compiled and minified JavaScript -->
                <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>

            </head>
            <body>
                <nav class="navbar navbar-dark bg-dark">
                  <a class="navbar-brand" href="/">Your Financial Keeper</a>
                  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarNavDropdown">
                    <ul class="navbar-nav">
                      <li class="nav-item active">
                        <a class="nav-link" href="/create">Join us<span class="sr-only">(current)</span></a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link" href="/about">About</a>
                      </li>
                        </div>
                      </li>
                    </ul>
                  </div>
                </nav>
            <div class="container">
                <div class="row">
                    <h1>
                    </h1>
                </div>
            </div>
            
            
            <div class="jumbotron">
  <h1 class="display-4">Hello, mate!</h1>
  <p class="lead">This program will provide you possibility to save all your expenses and incomes</p>
  <hr class="my-4">
  <p>It uses your personal data to analyze it and provide your detailed view of financial situaiton ocurred.</p>
  <p class="lead">
    <a class="btn btn-dark btn-lg" href="/create" role="button">Join us!</a>
  </p>
</div>
            




            </body>
        </html>"""
    index.encode(encoding='utf-8')
    return CONNECTION_OK, index


