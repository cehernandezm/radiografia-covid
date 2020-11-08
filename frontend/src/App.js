import './App.css';
import ImageUploader from 'react-images-upload';
import React, { Component } from 'react';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import Swal from 'sweetalert2'
import axios from 'axios';

class App extends Component {


  constructor() {
    super()
    this.onDrop = this.onDrop.bind(this)
    this.state = {
      pictures: [],
      loading: false
    }
    this.url = "http://35.225.76.77:5000/"
    document.title = "Covid-19 Analysis"
  }
  onDrop(picturesFiles, pictureDataURLs) {
    this.setState({
      pictures: picturesFiles
    })
  }

  componentDidMount() {
    this.onSubmit = this.onSubmit.bind(this)
  }

  onSubmit = e => {
    e.preventDefault()
    if (this.state.pictures.length > 0) {
      this.setState({ loading: true })
      let reader = new FileReader()
      reader.readAsDataURL(this.state.pictures[0])
      reader.onloadend = () => {
        axios.post(this.url, { imagen: reader.result })
          .then((res) => {
            this.setState({ loading: false })
            console.log(res.data)
            Swal.fire({
              title: 'Resultado',
              text: "La radiografia analizada es de tipo: " + res.data.msg,
              icon: 'success',
            })
          },
            (err) => {
              this.setState({ loading: false })
              console.log(err)
              Swal.fire({
                title: 'Error',
                text: "Ha ocurrido un error al analizar la imagen",
                icon: 'error',
              })
            })
      }
    }
    else {
      Swal.fire({
        title: 'Error',
        text: "Sube una imagen para analizar :(",
        icon: 'error',
      })
    }
  }
  render() {
    return (
      <div className="App container-fluid pt-5">
        <div className="row">
          <div className="col-12 text-left">
            <h1>COVID-19 Chest X-Ray Analysis</h1>
          </div>
        </div>
        <div className="row container mx-auto img-container">
          <div className="row container-fluid">
            <h6><span className="badge badge-danger">Disclaimer </span>
              <small>Es un proyecto totalmente educacional, es una red neuronal muy poco entrenada, los resultados no son exactos</small>

            </h6>

            <div className="col-12  w-100">
              <form onSubmit={this.onSubmit}>
                <ImageUploader className="upload"
                  singleImage={true}
                  withPreview={true}
                  withIcon={true}
                  buttonText='Subir Imagen'
                  onChange={this.onDrop}
                  imgExtension={['.jpg', '.png']}
                  maxFileSize={5242880}
                />
                <div className="mx-auto text-center">
                  <button type="submit" className="btn btn-primary">Analizar</button>
                </div>
              </form>
              {this.state.loading === true &&
                <div class="text-center pt-3">
                  <div class="spinner-border" role="status">
                    <span class="sr-only">Loading...</span>
                  </div>
                </div>
              }
            </div>
          </div>

          <div className="row">
            <div className="col-12">
              <b>Precision Covid</b> 90%<br />
              <b>Precision Normal</b> 93%<br />
              <b> Precision Viral Pneumonia</b> 93%<br />
            </div>
          </div>

        </div>

      </div>
    );
  }
}

export default App;
