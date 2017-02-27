const socket = window.io.connect('http://localhost:3000')

const { Component } = React

const Navigation = () => (
    <nav className="navbar navbar-inverse navbar-fixed-top">
      <div className="container">
        <div className="navbar-header">
          <button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span className="sr-only">Toggle navigation</span>
            <span className="icon-bar"></span>
            <span className="icon-bar"></span>
            <span className="icon-bar"></span>
          </button>
          <a className="navbar-brand" href="#">Quiz Assignment</a>
        </div>
        <div id="navbar" className="navbar-collapse collapse">
          <ul className="nav navbar-nav">
            <li className="active"><a href="#">Overview</a></li>
            <li><a href="#configure">Configure</a></li>
            <li><a href="#document">Document</a></li>
            <li className="dropdown">
              <a href="#more" className="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">More<span className="caret"></span></a>
              <ul className="dropdown-menu">
                <li><a href="#action">Action</a></li>
                <li><a href="#another-action">Another action</a></li>
                <li><a href="#something-else-here">Something else here</a></li>
                <li role="separator" className="divider"></li>
                <li className="dropdown-header">Nav header</li>
                <li><a href="#separated-link">Separated link</a></li>
                <li><a href="#one-more-separated-link">One more separated link</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
)

class App extends Component {

  state = {}

  componentDidMount = () => {
    socket.on('state', (data) => {
      console.log(data)
      // this.setState(data)
    })
  }

  render = () => {
    return (
      <div>
        <Navigation />
        <div className="container">
          <div className="row">
            <div className="col-md-6">
            </div>
            <div className="col-md-6">
            </div>
          </div>
        </div>
      </div>
    )
  }
}