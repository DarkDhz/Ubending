import { Component, OnInit } from '@angular/core';
import {AppComponent} from "../../app.component";
import axios from 'axios'

@Component({
  selector: 'app-prova2',
  templateUrl: './addItem.component.html',
  styleUrls: ['./addItem.component.css'],
})
export class addItemComponent implements OnInit {
  // @ts-ignore
  overlay:object;
  // @ts-ignore
  popup:object;
  // @ts-ignore
  btnAbrirPopup:object;
  // @ts-ignore
  btnCerrarPopup:object;
  state = {categories: []}
  constructor() { }

  ngOnInit(): void {
    const path = 'https://ubending3.herokuapp.com/categories'
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
  // @ts-ignore
  product_name = document.getElementById('product_name')
  // @ts-ignore
  product_img = document.getElementById('product_img')
  // @ts-ignore
  product_price = document.getElementById('product_price')
  // @ts-ignore
  product_desc = document.getElementById('product_desc')
  // @ts-ignore
  product_category = document.getElementById('product_category')
  // @ts-ignore
  product_state = document.getElementById('product_state')



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
  onProductName(event: any){
    // @ts-ignore
    this.product_name = (<HTMLInputElement>event.target).value
  }
  onProductPrice(event: any){
    // @ts-ignore
    this.product_price = Number((<HTMLInputElement>event.target).value)
  }
  onProductDesc(event: any){
    // @ts-ignore
    this.product_desc = (<HTMLInputElement>event.target).value
  }
  onProductCat(event: any){
    // @ts-ignore
    this.product_category = (<HTMLInputElement>event.target).value
  }
  onProductState(event: any){
    // @ts-ignore
    this.product_state = (<HTMLInputElement>event.target).value
  }

  onFile(event: any){
    // @ts-ignore
    event.target.files[0].name
  }
  postProduct(){
    // @ts-ignore
    if(product_name.value.length < 3){
      // @ts-ignore
      product_name.style.border = "2px solid red"
    }
    // @ts-ignore
    else if(!this.product_desc){
      // @ts-ignore
      product_name.style.border = "2px solid red"
    }
    // @ts-ignore
    else if(!this.product_name || this.product_name.length < 3){
      // @ts-ignore
      product_name.style.border = "2px solid red"
    }
    // @ts-ignore
    else if(isNaN(Number(product_price.value)) == true){
      // @ts-ignore
      product_price.style.border = "2px solid red"
    }

    // @ts-ignore
    else if(!this.product_category){
      // @ts-ignore
      product_category.style.border = "2px solid red"
    }


    else{
      // @ts-ignore
      console.log(this.product_name)

      var params = { name:  this.product_name, price: this.product_price,
        description: this.product_desc,category_id : this.product_category,state: 1,image : 1};
      console.log(params)

      const path = `https://ubending3.herokuapp.com/user/2/product`
      axios.post(path, params)
        .then((res) => {
          alert('SHOW UPDATE CORRECTAMENT')
        })
        .catch((error) => {
          console.error(error)
          alert('ERROR AL AFEGIR SHOW')
        })
      // @ts-ignore
      alert(product_name.value)
      // @ts-ignore

      alert(product_price.value)
      /*
      // @ts-ignore
      overlay.classList.remove('active');
      // @ts-ignore
      popup.classList.remove('active');
*/}




  }


}
