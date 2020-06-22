from variables import CONNECTION_OK


def about_view():
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
                <div class="col mb-5">
                
                <p>Program which helps you to control your budget and be more effective</p>
                <p>Financial literacy is the possession of the set of skills and knowledge that allows an individual to make informed and effective decisions with all of their financial resources. Raising interest in personal finance is now a focus of state-run programs in countries including Australia, Canada, Japan, the United States and the United Kingdom. Understanding basic financial concepts allows people to know how to navigate in the financial system. People with appropriate financial literacy training make better financial decisions and manage money better that those without such training.</p>
                <p>Below you can find examples of program</p>
              </div>
                
                
<div id="accordion">
  <div class="card">
    <div class="card-header" id="headingOne">
      <h5 class="mb-0">
        <button class="btn btn-outline-dark" data-toggle="collapse" data-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
          Example of table
        </button>
      </h5>
    </div>

    <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
      <div class="card-body">
      
                      <table class="table table-dark">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">Category</th>
                      <th scope="col">Classification</th>
                      <th scope="col">Money</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <th scope="row">1</th>
                      <td>products</td>
                      <td>expense</td>
                      <td>1000</td>
                    </tr>
                    <tr>
                      <th scope="row">2</th>
                      <td>salary</td>
                      <td>income</td>
                      <td>59000</td>
                    </tr>
                    <tr>
                      <th scope="row">3</th>
                      <td>car</td>
                      <td>expense</td>
                      <td>10000</td>
                    </tr>
                  </tbody>
                </table>
      
      </div>
    </div>
  </div>
  <div class="card">
    <div class="card-header" id="headingTwo">
      <h5 class="mb-0">
        <button class="btn btn-outline-dark collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
          Example of table with summary
        </button>
      </h5>
    </div>
    <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
      <div class="card-body">
        
                              <table class="table table-dark">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">User</th>
                      <th scope="col">Total income</th>
                      <th scope="col">Total expense</th>
                      <th scope="col">Balance</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <th scope="row">1</th>
                      <td>Mike</td>
                      <td>15000</td>
                      <td>15000</td>
                      <td>0</td>
                    </tr>

                  </tbody>
                </table>
          
      </div>
    </div>
  </div>
  <div class="card">
    <div class="card-header" id="headingThree">
      <h5 class="mb-0">
        <button class="btn btn-outline-dark collapsed" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
          Example of interface
        </button>
      </h5>
    </div>
    <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
      <div class="card-body">
      
      <div class="alert alert-danger" role="alert">
  <h4 class="alert-heading">Sorry!</h4>
  <p>Content at the moment is unavailable.</p>
  <hr>
  <p class="mb-0">We'll inform you via mail, when it will be ready.</p>
  <p class="mb-0">Just do not forget to join us</p>
</div>
      
      </div>
    </div>
  </div>
</div>
                </body>
            </html>"""
    about.encode(encoding='utf-8')
    return CONNECTION_OK, about
