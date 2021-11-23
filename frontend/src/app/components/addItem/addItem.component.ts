import {AfterViewInit, Component, OnInit} from '@angular/core';
import {AppComponent} from "../../app.component";
import axios from 'axios'
import {Router} from "@angular/router";
import {UploadService} from "../../services/upload.service";

@Component({
  selector: 'app-prova2',
  templateUrl: './addItem.component.html',
  styleUrls: ['./addItem.component.css'],
})
export class addItemComponent implements OnInit{


  category_id: number = -1;
  // @ts-ignore
  overlay:object;
  // @ts-ignore
  popup:object;
  // @ts-ignore
  btnAbrirPopup:object;
  // @ts-ignore
  btnCerrarPopup:object;
  state = {categories: []}

  token = "null";

  constructor(private router: Router, private uploadService: UploadService) {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
    } else {
      alert('NOT LOGGED IN')
      this.router.navigate(['/home']);
    }
  }

  ngOnInit(): void {
    const path = 'http://127.0.0.1:5000/categories'
    axios.get(path)
      .then((res) => {

        // @ts-ignore
        this.state.categories =  res.data
      })
      .catch((error) => {
        console.error(error)
      })
  }
  // @ts-ignore
  overlay = document.getElementById('overlay')
  // @ts-ignore
  popup = document.getElementById('popup')
  // @ts-ignore
  btnAbrirPopup = document.getElementById('btn-abrir-popup')
  // @ts-ignore
  btnCerrarPopup = document.getElementById('btn-cerrar-popup')
  // @ts-ignore
  selectedFiles : FileList;

  upload(filename: String) {
    const file = this.selectedFiles.item(0);
    // @ts-ignore
    const extension = file.type.split('/').pop();
    this.uploadService.uploadFile(file, filename + "." + extension);
  }

  // @ts-ignore
  selectFile(event) {
    this.selectedFiles = event.target.files;
  }

  open(){
    // @ts-ignore
    overlay.classList.add('active');
    // @ts-ignore
    popup.classList.add('active');
  }

  close(){
    // @ts-ignore
    popup.classList.remove('active');
    // @ts-ignore
    overlay.classList.remove('active');
  }

  selectCategory(event: any) {
    this.category_id = (<HTMLSelectElement>event.target).selectedIndex;
  }

  postProduct(){


    let product_name = (<HTMLInputElement>document.getElementById("product_name")).value;
    let product_price = (<HTMLInputElement>document.getElementById("product_price")).value;

    let product_state = (<HTMLSelectElement>document.getElementById("product_state")).selectedIndex;
    let product_desc = (<HTMLInputElement>document.getElementById("product_desc")).value;

    if (!product_name || !product_price || !product_desc || product_state == -1 || this.category_id == -1 || this.selectedFiles == undefined) {
      alert("invalid params")
    } else {
      const path = `http://127.0.0.1:5000/myproduct/` + this.token

      // @ts-ignore
      const params = {
        name: product_name,
        description: product_desc,
        price: product_price,
        state: product_state,
        // @ts-ignore
        image: this.selectedFiles.item(0).type.split('/').pop(),
        category_id: this.category_id
      }
      axios.post(path, params)
        .then((res) => {
          // @ts-ignore
          let id = res.data.product_id
          this.upload("product" + id)
          this.router.navigateByUrl('/', {skipLocationChange: true}).then(()=>
            this.router.navigate(['/user-products']));
        })
        .catch((error) => {
          console.error(error)
          alert('ERROR ADDING PRODUCT')
        })
    }
    // @ts-ignore






  }


}
