const socket = window.io.connect('http://localhost:3000')

const { Component } = React

/*
 * This is a simple input box for elastic search. Don't know what exactly is elastic search yet...
 */
const ElasticSearch = () => (
  <div className="input-group">
    <input type="text" className="form-control" placeholder="Search for..." />
    <span className="input-group-btn">
      <button className="btn btn-default" type="button">Go!</button>
    </span>
  </div>

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
      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <ElasticSearch />
          </div>
        </div>
      </div>
    )
  }
}