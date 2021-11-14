import { Component, OnInit } from '@angular/core';
import {AppComponent} from "../../app.component";
import axios from 'axios'

@Component({
  selector: 'app-prova2',
  templateUrl: './addItem.component.html',
  styleUrls: ['./addItem.component.css'],
})
export class addItemComponent implements OnInit {

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

  constructor() {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
    }

  }

  ngOnInit(): void {
    const path = 'https://ubending4.herokuapp.com/categories'
    axios.get(path)
      .then((res) => {

        // @ts-ignore
        this.state.categories =  res.data
        console.log(this.state.categories)
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
    //getted from event
    this.category_id = (<HTMLSelectElement>event.target).selectedIndex;
    //getted from binding
  }

  postProduct(){
    let product_name = (<HTMLInputElement>document.getElementById("product_name")).value;
    let product_price = (<HTMLInputElement>document.getElementById("product_price")).value;

    let product_state = (<HTMLSelectElement>document.getElementById("product_state")).selectedIndex;
    let product_desc = (<HTMLInputElement>document.getElementById("product_desc")).value;

    console.log(product_name)

    if (!product_name || !product_price || !product_desc || product_state == -1|| this.category_id == -1) {
      alert("invalid params")
    } else {
      const path = `http://127.0.0.1:5000/myproduct/` + this.token

      const params = {
        name: product_name,
        description: product_desc,
        price: product_price,
        state: product_state,
        category_id: this.category_id
      }
      axios.post(path, params)
        .then((res) => {
          alert('PRODUCT ADDED')
        })
        .catch((error) => {
          console.error(error)
          alert('ERROR ADDING PRODUCT')
        })
    }
    // @ts-ignore






  }


}
