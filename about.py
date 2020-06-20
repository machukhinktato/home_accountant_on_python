def about_view(request):
    about = """<!DOCTYPE html>
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
                    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
                </head>
                <body>
                    <nav class="navbar navbar-dark bg-dark">
                      <a class="navbar-brand" href="/">Financial Keeper - Home</a>
                      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                      </button>
                      <div class="collapse navbar-collapse" id="navbarNavDropdown">
                        <ul class="navbar-nav">

                          <li class="nav-item">
                            <a class="nav-link" href="#">Log In</a>
                            
                          </li>
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
                <div class="card" style="width: 18rem;">
                  <div class="card-body">
                    <h5 class="card-title">Financial keeper</h5>
                    <h6 class="card-subtitle mb-2 text-muted">About us</h6>
                    <p class="card-text">Program which helps you to control your budget and be more effective</p>
                    <a href="#" class="card-link">Create account</a>
                    <a href="#" class="card-link">Subscribe us</a>
                  </div>
                </div>
                </body>
            </html>"""
    about.encode(encoding='utf-8')
    return '200 OK', about